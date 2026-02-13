import os
from google.genai import types

schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Read the contents of a file",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(type=types.Type.STRING),
        },
        required=["file_path"],
    ),
)

def get_file_content(working_directory, file_path):
    # Compute project root based on THIS file's location
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    full_path = os.path.join(project_root, file_path)

    with open(full_path, "r") as f:
        return f.read()

