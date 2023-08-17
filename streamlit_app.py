import streamlit as st
import requests
import json

# Title of the application
st.title('Keyword-based Blog Generator')

# Text input for the user to enter keywords
keywords = st.text_input('Enter the keywords for the blog:')

# Button to generate the blog
if st.button('Generate Blog'):
    # Constructing the prompt
    prompt = f"Write a blog post about {keywords}"

    # API Endpoint
    url = "https://api.anthropic.com/v1/complete"

    # Headers
    headers = {
        'accept': 'application/json',
        'anthropic-version': '2023-06-01',
        'content-type': 'application/json',
        'x-api-key': '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' # Replace with your actual API key
    }

    # Data
    data = {
        "prompt": prompt,
        "max_tokens": 1000 # You can adjust this based on the desired length of the blog
    }

    # Sending POST request to Claude API
    response = requests.post(url, headers=headers, json=data)

    # Handling the response
    if response.status_code == 200:
        blog_content = json.loads(response.text).get('choices', [{}])[0].get('text', '')
        st.write(blog_content) # Displaying the generated blog content
    else:
        st.error(f"An error occurred: {response.text}")

