import openai
from openai import OpenAI
import os
import asyncio


def test():
    client = OpenAI(
        api_key=os.environ.get("OPENAI_API_KEY")
    )

    response = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": "Say this is a test",
            }
        ],
        model="gpt-3.5-turbo"
    )

    return response.choices[0].message.content


if __name__ == "__main__":
    print(test())