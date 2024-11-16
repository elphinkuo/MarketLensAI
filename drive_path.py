import os
import json
import openai
import base64

client = openai.OpenAI(
    api_key="3eeb5fff-f021-4ab7-b45b-61d8aa686b80",
    base_url="https://api.sambanova.ai/v1",
)

def get_base64_encoding(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')
    

image_path = "road_scenes/drive_scenes/drive_scene1.jpg"

image_base64 = get_base64_encoding(image_path)

prompt1 = "You are a mature driver behind the wheel. This image is the front view of the road you are driving on. Could you draw a driving path on the image to show how you would navigate through this road? If you could also provide the coordination of the path, that would be terrific!"

print("Question is {}", prompt1)

response = client.chat.completions.create(
    model='Llama-3.2-11B-Vision-Instruct',
    messages=[{"role":"user","content":[{"type":"text","text": prompt1},{"type":"image_url","image_url":{"url":f"data:image/png;base64,{image_base64}"}}]}],
    temperature =  0.1,
    top_p = 0.1
)

print(response.choices[0].message.content)