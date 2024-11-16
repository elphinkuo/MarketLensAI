import os
import json
import openai
import base64
import logging

# Configure logging to log errors
logging.basicConfig(level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')

# Initialize the OpenAI client with API key and base URL
client = openai.OpenAI(
    api_key="3eeb5fff-f021-4ab7-b45b-61d8aa686b80",
    base_url="https://api.sambanova.ai/v1",
)

def get_base64_encoding(image_path):
    # Read the image file and return its base64 encoding
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

# Process for surrounding 1
# Define the path to the first image
image_path = "road_scenes/reasoning/surrounding_views/surrounding_1.png"

# Get the base64 encoding of the first image
image_base64 = get_base64_encoding(image_path)

# Open and read the JSON file containing the first question
with open("road_scenes/reasoning/surrounding_views/surrounding_1.json", "r") as file:
    question1 = json.load(file)['question1']

# Print the first question
print("Question is {}", question1)

# Make a request to the chat completion API for the first question
response = client.chat.completions.create(
    model='Llama-3.2-11B-Vision-Instruct',
    messages=[{"role":"user","content":[{"type":"text","text": question1},{"type":"image_url","image_url":{"url":f"data:image/png;base64,{image_base64}"}}]}],
    temperature =  0.1,
    top_p = 0.1
)

# Print the response for the first question
print("Response is \n")
print(response.choices[0].message.content)
print("*" * 32)

# Open and read the JSON file containing the second question
with open("road_scenes/reasoning/surrounding_views/surrounding_1.json", "r") as file:
    question2 = json.load(file)['question2']

# Print the second question
print("Question is {}", question2)

# Make a request to the chat completion API for the second question
response = client.chat.completions.create(
    model='Llama-3.2-11B-Vision-Instruct',
    messages=[{"role":"user","content":[{"type":"text","text": question2},{"type":"image_url","image_url":{"url":f"data:image/png;base64,{image_base64}"}}]}],
    temperature =  0.1,
    top_p = 0.1
)

# Print the response for the second question
print("Response is \n")
print(response.choices[0].message.content)
print("*" * 32)

# Open and read the JSON file containing the third question
with open("road_scenes/reasoning/surrounding_views/surrounding_1.json", "r") as file:
    question3 = json.load(file)['question3']

# Print the third question
print("Question is {}", question3)

# Make a request to the chat completion API for the third question
response = client.chat.completions.create(
    model='Llama-3.2-11B-Vision-Instruct',
    messages=[{"role":"user","content":[{"type":"text","text": question3},{"type":"image_url","image_url":{"url":f"data:image/png;base64,{image_base64}"}}]}],
    temperature =  0.1,
    top_p = 0.1
)

# Print the response for the third question
print("Response is \n")
print(response.choices[0].message.content)
print("*" * 32)

# Process for surrounding 2
try:
    # Define the path to the second image
    image_path = "road_scenes/reasoning/surrounding_views/surrounding_2.png"
    
    # Get the base64 encoding of the second image
    image_base64 = get_base64_encoding(image_path)

    # Open and read the JSON file containing the first question for surrounding 2
    with open("road_scenes/reasoning/surrounding_views/surrounding_2.json", "r") as file:
        question1 = json.load(file)['dialog1']['question1']

    # Print the first question for surrounding 2
    print("Question is {}", question1)

    # Make a request to the chat completion API for the first question of surrounding 2
    response = client.chat.completions.create(
        model='Llama-3.2-11B-Vision-Instruct',
        messages=[{"role":"user","content":[{"type":"text","text": question1},{"type":"image_url","image_url":{"url":f"data:image/png;base64,{image_base64}"}}]}],
        temperature=0.1,
        top_p=0.1
    )

    # Check if the response is valid and print the content
    if response and response.choices and response.choices[0].message:
        print("Response is \n")
        print(response.choices[0].message.content)
    else:
        # Log an error if the response is invalid
        logging.error("Invalid response received from the API")
        logging.error("Full response: %s", response)

except FileNotFoundError as e:
    # Log an error if the file is not found
    logging.error("File not found: %s", e)
except json.JSONDecodeError as e:
    # Log an error if there is an issue decoding the JSON
    logging.error("Error decoding JSON: %s", e)
except Exception as e:
    # Log any other unexpected errors
    logging.error("An unexpected error occurred: %s", e)
finally:
    # Print a separator line
    print("*" * 32)