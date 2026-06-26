import streamlit as st
from google import genai
from google.genai import types
config = types.GenerateContentConfig(
    system_instruction = """.You are an expert Valve Analyst and Strategist.
 Answer only questions related to Valve Technology.
 For any non-Python question, reply exactly:
 Please ask a valve question.
 Do not answer questions outside the valve domain."""
  )
st.markdown(
  """
  <h1 style='text-align: center;'> VELAN INDIA's AI TOOL</h1>
  <p style='text-align: center; font-size:18px;'>
    Ask any question.
  </p>
  """,
  unsafe_allow_html=True,
)
chitti = genai.Client( api_key=st.secrets["API_KEY"])
mychat = chitti.chats.create(model="gemini-flash-lite-latest")

#Placeholder for the response
response_placeholder = st.empty()

question = st.text_input("", placeholder="Enter your Python question here...")

col1, col2, col3 = st.columns([4, 1, 4])

with col2:
  send =st.button("Send")
if send:
  response = mychat.send_message(question)
  response_placeholder.write(response.text)

mychat = robo.chats.create(model="gemini-flash-lite-latest")
#Placeholder for the response
response_placeholder = st.empty()

question = st.text_input("", placeholder="Enter your Python question here...")

col1, col2, col3 = st.columns([4, 1, 4])

with col2:
  send =st.button("Send")

if send:
  question = question + config.system_instruction
  response = mychat.send_message(question)
  response_placeholder.write(response.text)
