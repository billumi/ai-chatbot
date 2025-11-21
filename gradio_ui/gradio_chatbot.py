import os
import gradio as gr
from dotenv import load_dotenv
from openai import OpenAI

# Load API key
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def chat_with_llm(message, history):
    """
    This function receives the latest user message and chat history,
    sends it to the OpenAI API, and returns the updated history.
    """

    # Rebuild conversation for OpenAI API
    messages = [{"role": "system", "content": "You are a helpful chatbot."}]

    # Add previous messages from history
    for user_msg, bot_msg in history:
        messages.append({"role": "user", "content": user_msg})
        messages.append({"role": "assistant", "content": bot_msg})

    # Add new message
    messages.append({"role": "user", "content": message})

    # Call LLM
    response = client.chat.completions.create(
        model="gpt-4o-mini",  # or gpt-5.1, gpt-4.1, gpt-4o, etc.
        messages=messages
    )

    bot_answer = response.choices[0].message.content

    # Append to history
    history.append((message, bot_answer))
    return history, history


# Build Gradio UI
with gr.Blocks(theme="soft") as demo:
    gr.Markdown("## 🤖 Gradio LLM Chatbot")
    
    chatbot = gr.Chatbot(height=400)
    user_input = gr.Textbox(label="Type your message")
    
    clear_btn = gr.Button("Clear Chat")

    user_input.submit(chat_with_llm, [user_input, chatbot], [chatbot, chatbot])
    clear_btn.click(lambda: None, None, chatbot, queue=False)

# Run Gradio app
if __name__ == "__main__":
    demo.launch()

