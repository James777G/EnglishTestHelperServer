import base64
import requests
import os

api_key = os.getenv("OPENAI_API_KEY")


def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')


def generate_english_test_answer(image_paths, client):
    base64_images = [encode_image(image_path) for image_path in image_paths]

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }

    messages = [
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "Help my grandma to complete ALL the English questions in the images with "
                            "well-formatted answers. Answer the questions in the format "
                            "Question:  \n\n"
                            "Answer:    \n\n. Don't include introduction in the response, only answers to the "
                            "questions are needed",
                }
            ],
        }
    ]

    for base64_image in base64_images:
        messages.append({
            "role": "user",
            "content": [
                {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{base64_image}"}},
            ],
        })

    payload = {
        "model": "gpt-4-vision-preview",
        "messages": messages,
        "max_tokens": 1000,
    }

    response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)

    response_data = response.json()

    # Extracting the completed answer from the response
    completed_answer = response_data['choices'][0]['message']['content']

    print(completed_answer)

    return completed_answer
