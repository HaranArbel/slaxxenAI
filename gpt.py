from openai import OpenAI
import os

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY")
)


def process_message_with_gpt(slack_messages: str):

    content = f'''
            What were the primary issues discussed in the Slack channels during this time frame? What were the key updates and resolutions provided for each issue?
            Try to describe problems only, for each main problem please provide a breakdown that will include:
            Root Problem / cause Identification:
            Define the problem briefly, including the start time or the time the issue was first reported.
            Key Participants:
            List the individuals involved or those who reported the issue.
            Detailed Description:
            Offer a comprehensive but concise explanation of the problem, its impact, and any initial observations or suspected causes.
            Steps Taken or Resolution Attempts:
            Outline the steps or actions taken to address the issue, including any troubleshooting or investigation efforts.
            Linked issues:
            Add the short description for linked / sub issues or any other side effects
            Current Status:
            Provide the current state of the problem or the status of the resolution, highlighting any progress made or ongoing efforts.
            Individuals Resolving the Issue:
            Mention the names or teams actively involved in resolving the problem.
            "
            {slack_messages}
            "'''

    response = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": content,
            }
        ],
        model="gpt-3.5-turbo"
    )

    return response.choices[0].message.content
