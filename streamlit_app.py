import streamlit as st
import requests

# Title of the Streamlit application
st.title("Keyword-based Blog Generator")

# Input for keywords
keywords = st.text_input('Enter the keywords for the blog:')

# Configuration
url = "https://api.promptperfect.jina.ai/q2jb2ZpjQ23hUPjN4Xza"
headers = {
    "Content-Type": "application/json"
}

# Function to call the API
def generate_blog(keywords):
    response = requests.post(url, headers=headers, json={"parameters": {"Keywords": keywords}})
    if response.status_code == 200:
        return response.json()
    else:
        return response.text

# Generate blog button
if st.button('Generate Blog'):
    result = generate_blog(keywords)
    st.write(result)  # Displaying the generated blog content
