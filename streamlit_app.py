import streamlit as st
from chatbots.claude import Claude

# Configuration
ANTHROPIC_API_KEY = "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"  # Replace with your actual API key
model = "claude-2"  # You can replace this with your desired model
temperature = 0.1

st.title("Keyword-based Blog Generator")

# Initialization
if "bot" not in st.session_state:
    st.session_state.bot = Claude(api_key=ANTHROPIC_API_KEY, model=model, temperature=temperature)

# Input for keywords
keywords = st.text_input('Enter the keywords for the blog:')

# Generate blog button
if st.button('Generate Blog'):
    # Constructing the prompt
    prompt = f"Write a blog post about {keywords}"

    # Generating the blog content
    full_response = ""
    for response in st.session_state.bot.ask_llm(prompt, stream=True):
        full_response += response

    st.write(full_response)  # Displaying the generated blog content
