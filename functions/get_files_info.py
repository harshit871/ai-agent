# The key idea is that the directory parameter will be treated as a relative path within the working_directory. 
# We'll allow the LLM agent to specify which directory it wants to scan, but the working_directory will be set by us. 
# This means we can limit the scope of directories and files that the LLM is able to view.
import os

def get_files_info(working_directory, directory="."):
    working_dir_abs = os.path.abspath(working_directory) # to get the absolute path of the working_directory.
    target_dir = os.path.normpath(os.path.join(working_dir_abs, directory))

    # Will be True or False
    valid_target_dir = os.path.commonpath([working_dir_abs, target_dir]) == working_dir_abs
    if not valid_target_dir:
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    
    if not os.path.isdir(target_dir):
        return f'Error: "{directory}" is not a directory'
    
    try:
        directory_contents = os.listdir(target_dir)

        all_paths = []
        for file in directory_contents:
            full_path = os.path.join(target_dir, file)
            
            all_paths.append(f"- {file}: file_size={os.path.getsize(full_path)} bytes, is_dir={os.path.isdir(full_path)}")
    except Exception as e:
        return f"Error: {str(e)}"
    

    return ('\n').join(all_paths)
