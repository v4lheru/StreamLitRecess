import streamlit as st
from anthropic import Claude2
from langchain import PromptTemplate

st.set_page_config(page_title="🦜🔗 Blog Outline Generator App")
st.title('🦜🔗 Blog Outline Generator App')
anthropic_api_key = st.sidebar.text_input('Anthropic API Key', type='password')

def generate_response(topic):
  claude2_model = Claude2(model_name='claude-2', anthropic_api_key=anthropic_api_key)
  # Prompt
  template = 'As an experienced data scientist and technical writer, generate an outline for a blog about {topic}.'
  prompt = PromptTemplate(input_variables=['topic'], template=template)
  prompt_query = prompt.format(topic=topic)
  # Run Claude-2 model and print out response
  response = claude2_model(prompt_query)
  return st.info(response)

with st.form('myform'):
  topic_text = st.text_input('Enter keyword:', '')
  submitted = st.form_submit_button('Submit')
  if not anthropic_api_key.startswith('sk-'):
    st.warning('Please enter your Anthropic API key!', icon='⚠')
  if submitted and anthropic_api_key.startswith('sk-'):
    generate_response(topic_text)
