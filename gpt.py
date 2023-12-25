from openai import OpenAI
import os

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY")
)


def process_message_with_gpt(message: str):
    response = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": message,
            }
        ],
        model="gpt-3.5-turbo"
    )

    return response.choices[0].message.content
