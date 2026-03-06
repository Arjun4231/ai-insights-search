import streamlit as st
import langchain_helper
from config import project_title

st.title(project_title)

query = st.text_input("Write Your Query")

if query:
    response = langchain_helper.answer_query(query)
    st.header('Answer')
    st.write(response)

