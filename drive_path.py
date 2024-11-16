import os
import json
import openai
import base64

# Initialize the OpenAI client with API key and base URL
client = openai.OpenAI(
    api_key="3eeb5fff-f021-4ab7-b45b-61d8aa686b80",
    base_url="https://api.sambanova.ai/v1",
)

def get_base64_encoding(image_path):
    """
    Read the image file and return its base64 encoding.
    
    Args:
        image_path (str): The path to the image file.
        
    Returns:
        str: The base64 encoded string of the image.
    """
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

# Define the path to the image
image_path = "road_scenes/drive_scenes/drive_scene1.jpg"

# Get the base64 encoding of the image
image_base64 = get_base64_encoding(image_path)

# Define the prompt for the API
prompt1 = "You are a mature driver behind the wheel. This image is the front view of the road you are driving on. Could you draw a driving path on the image to show how you would navigate through this road? If you could also provide the coordination of the path, that would be terrific!"

# Print the prompt
print("Question is {}", prompt1)

# Make a request to the chat completion API
response = client.chat.completions.create(
    model='Llama-3.2-11B-Vision-Instruct',
    messages=[{"role":"user","content":[{"type":"text","text": prompt1},{"type":"image_url","image_url":{"url":f"data:image/png;base64,{image_base64}"}}]}],
    temperature=0.1,
    top_p=0.1
)

# Print the response content
print(response.choices[0].message.content)