import streamlit as st
import requests

# Configuration
YOUR_GENERATED_SECRET = "CIRhQqBVNwVwTEeB7qsV:e7cfa93256ee61392eea569109d7ecf0df1257217da729f6b9068c2565079948"
url = "https://api.promptperfect.jina.ai/q2jb2ZpjQ23hUPjN4Xza"
headers = {
    "x-api-key": f"token {YOUR_GENERATED_SECRET}",
    "Content-Type": "application/json"
}

# Title of the Streamlit application
st.title("Keyword-based Blog Generator with Claude")

# Input for keywords
keywords = st.text_input('Enter the keywords for the blog:')

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
