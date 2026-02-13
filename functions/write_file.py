import os
from google.genai import types

schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Write text to a file",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(type=types.Type.STRING),
            "content": types.Schema(type=types.Type.STRING),
        },
        required=["file_path", "content"],
    ),
)

def write_file(working_directory, file_path, content):
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    full_path = os.path.join(project_root, file_path)


    with open(full_path, "w") as f:
        f.write(content)
    return f"Wrote to {file_path}"


