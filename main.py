import openai
from openai import OpenAI
import os
from fastapi import FastAPI
import asyncio

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}


#
# def test():
#     client = OpenAI(
#         api_key=os.environ.get("OPENAI_API_KEY")
#     )
#
#     response = client.chat.completions.create(
#         messages=[
#             {
#                 "role": "user",
#                 "content": "Say this is a test",
#             }
#         ],
#         model="gpt-3.5-turbo"
#     )
#
#     return response.choices[0].message.content


# if __name__ == "__main__":
    # print(test())
    # messages = [
    #     '''[You, 10:05 AM]
    #         Hey team, I've encountered a few issues that need our attention. The first one is regarding the new deployment script. It seems to be failing at the authentication step. I've double-checked the credentials, but something's still off.
    #     ''',
    #     '''
    #         [Team Member 1, 10:06 AM]
    #         Good catch! Did you check if the API keys were updated recently?
    #     ''',
    #     '''
    #         [Team Member 2, 10:07 AM]
    #         I'll take a look at the deployment logs. Maybe there's something we're missing.
    #     ''',
    #
    # ]
