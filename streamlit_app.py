import streamlit as st
import requests

API_URL = "https://flowise-production-647d.up.railway.app/api/v1/prediction/52211d51-9c75-4e75-9331-1f5d76a3a5fa"

def query(payload):
    response = requests.post(API_URL, json=payload)
    return response.json()

def generate_response(topic):
    # Prompt
    template = 'As an experienced data scientist and technical writer, generate an outline for a blog about {topic}.'
    prompt_query = template.format(topic=topic)
    # Query Claude-2 model using Flowise API and print out response
    response = query({"question": prompt_query})
    return st.info(response['answer'])  # Assuming 'answer' key in the response

st.set_page_config(page_title="🦜🔗 Blog Outline Generator App")
st.title('🦜🔗 Blog Outline Generator App')

with st.form('myform'):
    topic_text = st.text_input('Enter keyword:', '')
    submitted = st.form_submit_button('Submit')
    if submitted:
        generate_response(topic_text)
