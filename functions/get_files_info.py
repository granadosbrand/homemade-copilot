import os

def get_files_info(working_directory, directory=None):
    
    if directory is None:
        directory = working_directory

    abs_full_path = os.path.abspath(os.path.join(working_directory, directory))
    
    if not abs_full_path.startswith(os.path.abspath(working_directory)):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        
    if not os.path.isdir(abs_full_path):
        return f'Error: "{directory}" is not a directory'


    try:
        files_result = []
        for file in os.listdir(abs_full_path):
            file_path = os.path.join(abs_full_path, file)
            files_result.append({
                'filename' : file,
                'file_size' : os.path.getsize(file_path),
                'is_dir' : not os.path.isfile(file_path)
            })
        result = ''
        for file in files_result:
            result = result +  f"- {file['filename']}: file_size={file['file_size']} bytes, is_dir={file['is_dir']}\n"      
        return result
    except Exception as e:
        return f'Error: {str(e)}'
