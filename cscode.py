import streamlit as st
from google import genai
from google.genai import types

config = types.GenerateContentConfig(
    system_instruction=""".You are an expert Valve Analyst and Strategist.
 Answer only questions related to Valve Technology.
 For any non-valve question, reply exactly:
 Please ask a valve question.
 Do not answer questions outside the valve domain."""
)

st.markdown(
    """
  <h1 style='text-align: center;'> VELAN INDIA's AI TOOL</h1>
  <p style='text-align: center; font-size:18px;'>
    Ask any question related to our valves.
  </p>
  """,
    unsafe_allow_html=True,
)

chitti = genai.Client(api_key=st.secrets["API_KEY"])

# --- FIRST BLOCK: Valve Questions ---
mychat = chitti.chats.create(model="gemini-flash-lite-latest")
response_placeholder = st.empty()

question = st.text_input("", placeholder="Enter your Valve question here...")

col1, col2, col3 = st.columns([4, 1, 4])

with col2:
    send = st.button("Send")

if send:
    response = mychat.send_message(question)
    response_placeholder.write(response.text)


# --- SECOND BLOCK: Valve Questions ---
mychat_valve = chitti.chats.create(model="gemini-flash-lite-latest")
response_placeholder_valve = st.empty()

question_valve = st.text_input(
    "", placeholder="Enter your Valve question here...", key="valve_question"
)

# Added a unique key to the columns to prevent layout-level ID duplication
col1_py, col2_py, col3_py = st.columns([4, 1, 4], key="valve_cols")

with col2_py:
    send_python = st.button("Send", key="valve_send")

if send_python:
    # Fixed the variable naming mismatch here
    final_question = question_valve + config.system_instruction
    response = mychat_valve.send_message(final_question)
    response_placeholder_valve.write(response.text)
