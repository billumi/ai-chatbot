import os
from dotenv import load_dotenv
from openai import OpenAI

# Load API key
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def chat_with_llm():
    print("==== LLM Chatbot (Hello World) ====")
    print("Type 'exit' to quit.\n")

    while True:
        user_input = input("You: ")

        if user_input.lower() in ["exit", "quit"]:
            print("Chatbot: Goodbye!")
            break

        response = client.chat.completions.create(
            model="gpt-4o-mini",          # or gpt-5.1, gpt-4o, etc.
            messages=[
                {"role": "system", "content": "You are a friendly chatbot."},
                {"role": "user", "content": user_input}
            ]
        )

        answer = response.choices[0].message.content
        print(f"Chatbot: {answer}\n")


if __name__ == "__main__":
    chat_with_llm()

