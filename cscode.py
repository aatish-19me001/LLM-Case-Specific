import streamlit as st
from google import genai
from google.genai import types

# Define your system instruction configuration
config = types.GenerateContentConfig(
    system_instruction=""".You are an expert Valve Analyst and Strategist.
 Answer only questions related to Valve Technology.
 For any non-valve question, reply exactly:
 Please ask a valve question.
 Do not answer questions outside the valve domain."""
)

# Render the title header
st.markdown(
    """
  <h1 style='text-align: center;'> VELAN INDIA's AI TOOL</h1>
  <p style='text-align: center; font-size:18px;'>
    Ask any question related to our valves.
  </p>
  """,
    unsafe_allow_html=True,
)

# Initialize the Gemini client
chitti = genai.Client(api_key=st.secrets["API_KEY"])

# Initialize the chat session
mychat = chitti.chats.create(model="gemini-flash-lite-latest")

# Placeholder where the AI's response will appear
response_placeholder = st.empty()

# Single text input for the user
question = st.text_input("", placeholder="Enter your Valve question here...")

# Centered "Send" button layout
col1, col2, col3 = st.columns([4, 1, 4])

with col2:
    send = st.button("Send")

# Handle the button click event
if send and question:
    # Append the system instruction constraints to the question
    final_question = question + config.system_instruction
    
    # Send the message and display the output
    response = mychat.send_message(final_question)
    response_placeholder.write(response.text)
