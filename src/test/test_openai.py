from openai import OpenAI
# import os

# os.environ["OPENAI_API_BASE"] = "https://api.openai-proxy.org/v1"
# os.environ["OPENAI_API_KEY"] = "sk-JaRwWMSpa2er1CxmbklRQC0AmSnSJf7a4i02z7HwFnm6g5Zu"


# Initialize the OpenAI client
# client = OpenAI()

client = OpenAI(
    base_url='https://api.openai-proxy.org/v1',
    api_key='sk-JaRwWMSpa2er1CxmbklRQC0AmSnSJf7a4i02z7HwFnm6g5Zu',
)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "Say hi",
        }
    ],
    model="gpt-3.5-turbo",
)

print(chat_completion)