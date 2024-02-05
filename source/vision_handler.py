import base64
import requests
import os
from dotenv import load_dotenv
from source.files_handler import list_files
from source.files_handler import get_user_directory

def handle_vision():
    # Set your OpenAI API key in .env
    load_dotenv()
    api_key = os.getenv("API_KEY")

    def encode_image(image_path):
        with open(image_path, "rb") as image_file:
            return base64.b64encode(image_file.read()).decode('utf-8')

    user_directory = get_user_directory()
    image_paths = list_files(user_directory)

    results = []

    for image_path in image_paths:
        base64_image = encode_image(image_path)
        
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}"
        }

        payload = {
            "model": "gpt-4-vision-preview",
            "messages": [
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": "Create a new file name for this image by providing a brief description of it. Don't include a file extension."
                        },
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": f"data:image/jpeg;base64,{base64_image}"
                            }
                        }
                    ]
                }
            ],
            "max_tokens": 300
        }
        
        response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)
        
        response_json = response.json()
        
        results.append(response_json['choices'][0]['message']['content'] + os.path.splitext(image_path)[1])
        
        print(results)
    return {"results": results, "user_directory": user_directory}

# Credit to Umer Waqas for his bulk OpenAI Vision tutorial.