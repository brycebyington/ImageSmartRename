from source.vision_handler import handle_vision
from source.files_handler import rename_files

response = handle_vision()
rename_files(response["results"], response["user_directory"])

