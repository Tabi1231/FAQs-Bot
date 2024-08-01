import openai
import gradio as gr

# Set your OpenAI API key
openai.api_key = "sk----------------------------------------------------------"  # Replace this with your API key

# Initialize conversation history with a system message
conversation_history = [
    {"role": "system", "content": "Hi ChatGPT, you are a friendly and helpful assistant!"},
]

def get_chat_response(conversation):
    """
    Get a response from ChatGPT based on the conversation history.
    """
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=conversation
        )
        return response["choices"][0]["message"]["content"]
    except Exception as e:
        return f"Oops! Something went wrong. Please make sure your API key is set correctly. Error: {e}"

def chat_with_gpt(user_input):
    """
    Handle user input and generate a response from ChatGPT.
    """
    global conversation_history
    
    if user_input.lower() == "clear":
        conversation_history = [
            {"role": "system", "content": "Hi ChatGPT, you are a friendly and helpful assistant!"},
        ]
        initial_reply = get_chat_response(conversation_history)
        conversation_history.append({"role": "assistant", "content": initial_reply})
        return initial_reply
    elif user_input.lower() == "exit":
        return "Goodbye! Have a great day!"

    conversation_history.append({"role": "user", "content": user_input})
    chat_reply = get_chat_response(conversation_history)
    conversation_history.append({"role": "assistant", "content": chat_reply})
    return chat_reply

# Create the Gradio interface
iface = gr.Interface(
    fn=chat_with_gpt,
    inputs=gr.Textbox(lines=7, placeholder="Enter your message here...", label="You:"),
    outputs=gr.Textbox(label="ChatGPT:"),
    live=True,
    title="Friendly ChatGPT Assistant",
    description="Enter your message and get a friendly response from ChatGPT. Type 'clear' to reset the conversation or 'exit' to end the chat.",
)

# Launch the interface
iface.launch()
