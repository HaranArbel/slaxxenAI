from fastapi import FastAPI
from gpt import client, process_message_with_gpt

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/test")
async def process_message(chat_message: str):
    return process_message_with_gpt(chat_message.message)


