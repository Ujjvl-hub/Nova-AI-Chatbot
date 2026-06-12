from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI
from langchain_core.messages import (
    SystemMessage,
    HumanMessage,
    AIMessage
)

load_dotenv()

chat_model = ChatMistralAI(
    model="mistral-small-latest",
    temperature=0.7
)

messages = [
    SystemMessage(
        content="""
        You are Nova, a helpful AI assistant.
        Always respond in English by default.

        Only switch to another language if the user explicitly asks.
        """
    )
]

print("----------WELCOME-----------")
print("Enter 0 to end chats")

while True:
    prompt = input("You: ")

    if prompt == "0":
        break

    messages.append(HumanMessage(content=prompt))

    response = chat_model.invoke(messages)

    print("Nova:", response.content)

    messages.append(
        AIMessage(content=response.content)
    )