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


# surrounding 1
image_path = "road_scenes/reasoning/surrounding_views/surrounding_1.png"

image_base64 = get_base64_encoding(image_path)

with open("road_scenes/reasoning/surrounding_views/surrounding_1.json", "r") as file:
    question1 = json.load(file)['question1']

print("Question is {}", question1)

response = client.chat.completions.create(
    model='Llama-3.2-11B-Vision-Instruct',
    messages=[{"role":"user","content":[{"type":"text","text": question1},{"type":"image_url","image_url":{"url":f"data:image/png;base64,{image_base64}"}}]}],
    temperature =  0.1,
    top_p = 0.1
)

print("Responsie is \n")
print(response.choices[0].message.content)
print("*" * 32)

with open("road_scenes/reasoning/surrounding_views/surrounding_1.json", "r") as file:
    question2 = json.load(file)['question2']

print("Question is {}", question2)

response = client.chat.completions.create(
    model='Llama-3.2-11B-Vision-Instruct',
    messages=[{"role":"user","content":[{"type":"text","text": question2},{"type":"image_url","image_url":{"url":f"data:image/png;base64,{image_base64}"}}]}],
    temperature =  0.1,
    top_p = 0.1
)

print("Responsie is \n")
print(response.choices[0].message.content)
print("*" * 32)

# surrounding 2
# image_path = "road_scenes/reasoning/surrounding_views/surrounding_2.png"

# image_base64 = get_base64_encoding(image_path)

# response = client.chat.completions.create(
#     model='Llama-3.2-11B-Vision-Instruct',
#     messages=[{"role":"user","content":[{"type":"text","text":"You are a mature driver behind the wheel. These six images were captured and put together by the surround view camera in your vehicle. The FOV of each surround view camera is approximately 120°. And the middle two images are the directly front.\n Please describe in detail the scenario you are in, make a special distinction between what's in front of you and what's on either side of you!",
#     "answer": "You're in a mostly empty urban area with roads bordered by structures and some greenery. \n Directly in front: There's a relatively wide road with a few lane markings. Directly ahead, there's a large modern building with a unique architectural design featuring angled glass panels. To the left of the road, there are barriers indicating construction or some restricted area. There's a parked car on the right of these barriers. On the far left of the road, there's another street branching out. \n To the left: The beginning of a pedestrian crosswalk is visible, leading towards a traffic island with some trees. On the far side, there's a street that turns to the left with another building in the background. \n To the right: There's a continuation of the pedestrian crosswalk. Further right, a road intersects the one you're on, with a sign indicating a left turn. There are barriers similar to the ones directly in front of you. On the far right, you can see the corner of another building. \n At the back: It seems like you've just passed a junction. There are more road barriers and markings. On the left side of the road, there's a structure that appears to be a bus stop or a shelter. Further back, there's another large building and a traffic light. On the right side, you can see a continuation of the road you're on, flanked by more buildings."},{"type":"image_url","image_url":{"url":f"data:image/png;base64,{image_base64}"}}]}],
#     temperature =  0.1,
#     top_p = 0.1
# )

      