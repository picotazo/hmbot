import os
from google.genai import types

schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="List files in a directory",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(type=types.Type.STRING),
        },
    ),
)

def get_files_info(working_directory, directory="."):
    try:
        working_abs = os.path.abspath(working_directory)
        target_abs = os.path.abspath(os.path.join(working_abs, directory))

        # Prevent escaping the working directory
        if os.path.commonpath([working_abs, target_abs]) != working_abs:
            return f'Error: Cannot list "{directory}" because it is outside the working directory'

        if not os.path.isdir(target_abs):
            return f'Error: "{directory}" is not a directory'

        entries = []
        for name in os.listdir(target_abs):
            full_path = os.path.join(target_abs, name)
            entries.append({
                "name": name,
                "file_size": os.path.getsize(full_path),
                "is_dir": os.path.isdir(full_path),
            })

        return entries

    except Exception as e:
        return f"Error: {e}"

