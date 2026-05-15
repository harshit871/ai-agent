from config import MAX_CHARS
import os

def get_file_content(working_directory, file_path):
    working_dir_abs = os.path.abspath(working_directory) # to get the absolute path of the working_directory.
    target_file_path = os.path.normpath(os.path.join(working_dir_abs, file_path))

    # Will be True or False
    valid_target_file_path = os.path.commonpath([working_dir_abs, target_file_path]) == working_dir_abs
    if not valid_target_file_path:
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

    if not os.path.isfile(target_file_path):
        return f'Error: File not found or is not a regular file: "{file_path}"'
    
    try:
        with open(target_file_path, "r") as f:
            file_content_string = f.read(MAX_CHARS)
            # After reading the first MAX_CHARS...
            remainder = f.read(1)
            if remainder:
                file_content_string += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
    except Exception as e:
        return f"Error: {str(e)}"
    
    return file_content_string
    


