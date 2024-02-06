import streamlit as st
from langchain.llms import OpenAI

st.title("🦜🔗 StarlinkTuc App")

with st.sidebar:
    openai_api_key = st.text_input("OpenAI API Key", type="password")
    "[Adquiere Gratis una OpenAI API key, no hace falta tarjeta.](https://platform.openai.com/account/api-keys)"


def generate_response(input_text):
    llm = OpenAI(temperature=0.7, openai_api_key=openai_api_key)
    st.info(llm(input_text))


with st.form("my_form"):
    text = st.text_area("Enter text:", "¿Cuáles son las 3 primeras reglas de oro para el hombre?")
    submitted = st.form_submit_button("Submit")
    if not openai_api_key:
        st.info("sk-xxxxxxxxxx")
    elif submitted:
        generate_response(text)
