import openai
from openai import OpenAI


def generate_english_test_answer(question):
    client = OpenAI()
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system",
             "content": "You are an assistant helping my grandma who is learning english and needs well formatted "
                        "answers with their English test."},
            {"role": "user", "content": question}
        ]
    )

    return completion.choices[0].message.content

