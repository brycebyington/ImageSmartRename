import os

def list_files(user_directory):
    directory = user_directory
    file_paths = []
    
    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)
        if os.path.isfile(f) and (f.endswith('.png') or f.endswith('.jpg')):
            print(f)
            file_paths.append(f)
            
    return file_paths

def get_user_directory():
    user_directory = input("Enter the directory in which you want files to be renamed: ")
    
    return user_directory

def rename_files(results, user_directory):
    
    current_file_paths = list_files(user_directory)
    
    if len(current_file_paths) != len(results):
        print("Error: The number of files and the number of new names do not match.")
        return

    for i, file_path in enumerate(current_file_paths):
        new_name = results[i]
        new_file_path = os.path.join(user_directory, new_name)

        os.rename(file_path, new_file_path)
        print(f"Renamed {file_path} to {new_file_path}")