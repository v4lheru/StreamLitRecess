import streamlit as st
import requests

API_URL = "https://flowise-production-647d.up.railway.app/api/v1/prediction/52211d51-9c75-4e75-9331-1f5d76a3a5fa"
headers = {"Authorization": "Bearer sYw5pht0ophm4MHnY48EGWAWEuRbeAkvtoKImlVexio="}

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    print(f"API Response: {response.status_code} - {response.text}")
    
    try:
        return response.json()
    except ValueError:
        return {"error": f"Unexpected response from API. Status Code: {response.status_code}"}

def main():
    st.title("Input Fields with API Integration")

    number_of_fields = st.session_state.get("number_of_fields", 1)

    # Create dynamic input fields based on the number
    all_inputs = []
    for i in range(number_of_fields):
        user_input = st.text_input(f"Input {i+1}")
        all_inputs.append(user_input)

    # Buttons to add and remove fields
    col1, col2, col3 = st.columns(3)

    if col1.button("+ Add"):
        number_of_fields += 1
        st.session_state.number_of_fields = number_of_fields

    if col2.button("- Remove") and number_of_fields > 1:
        all_inputs.pop()  # Remove the last entry
        number_of_fields -= 1
        st.session_state.number_of_fields = number_of_fields

    # Button to trigger API call
    if st.button("Submit"):
        combined_input = ". ".join([f"{idx+1}. {input_}" for idx, input_ in enumerate(all_inputs)])
        
        payload = {"question": combined_input}
        response = query(payload)

        if isinstance(response, dict):  # If response is a dictionary
            if "error" in response:
                final_response = response["error"]
            else:
                final_response = response.get('response', 'No response')
        else:
            final_response = str(response)

        # Display the response in a larger text box
        st.text_area("Response", value=final_response, height=300)
