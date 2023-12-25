from fastapi import FastAPI
from gpt import client, process_message_with_gpt
from pydantic import BaseModel


app = FastAPI()


class SlackMessage(BaseModel):
    slack_messages: str


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/process_messages")
async def process_message(slack_message: SlackMessage):
    return process_message_with_gpt(slack_message.slack_messages)
