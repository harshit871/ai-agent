import os
import subprocess

def run_python_file(working_directory, file_path, args=None):
    working_dir_abs = os.path.abspath(working_directory) # to get the absolute path of the working_directory.
    target_file_path = os.path.normpath(os.path.join(working_dir_abs, file_path))

    valid_target_file_path = os.path.commonpath([working_dir_abs, target_file_path]) == working_dir_abs
    if not valid_target_file_path:
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    
    if not os.path.isfile(target_file_path):
        return f'Error: "{file_path}" does not exist or is not a regular file'
    
    if not target_file_path.endswith('.py'):
        return f'Error: "{file_path}" is not a Python file'
    
    command = ["python", target_file_path]

    if args:
        command.extend(args)
    
    try:
        completed_process = subprocess.run(command, capture_output=True, text=True, timeout=30)

        stdout = completed_process.stdout
        stderr = completed_process.stderr
        returncode = completed_process.returncode

        output_msg = ''
        if returncode != 0:
            output_msg += "Process exited with code X"
        
        if not stdout and not stderr:
            output_msg += "No output produced"
        
        if stdout:
            output_msg += f'STDOUT: {stdout}'
        
        if stderr:
            output_msg += f'STDERR: {stderr}'
        
        return output_msg
    except Exception as e:
        return f"Error: executing Python file: {e}"

    
