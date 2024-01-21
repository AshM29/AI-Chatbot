feom dotenv import load_dataenv
load_dotenv()

import os
import google.generativeai as genai
import streamlit as st
model=genai.configure(api_key="GOOGLE_API_KEY")
chat=genai.start_chat(history=[])

def get_gemini_response(question):
  response=chat.send_message(stream=True)
  return response
  
st._config("Q&A Chatbot")
st.header("Conversational ChatBot")

if 'chat_history' not in st.session_state['chat_history']:
    st.session_state['chat_history']= []

input=st.text_input("Input: ",key="input")
submit=st.button("Send")

if input and submit:
  response=get_gemini_response(input)
  st.session_state['chat_history'].append(("You",input))
  
