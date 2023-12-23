import streamlit as st
from langchain.llms import OpenAI

st.title("🦜🔗 OpenAI con Langchain")

with st.sidebar:
    openai_api_key = st.text_input("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
", type="password")
    "[Get an OpenAI API key](https://platform.openai.com/account/api-keys)"


def generate_response(input_text):
    llm = OpenAI(temperature=0.7, openai_api_key=openai_api_key)
    st.info(llm(input_text))


with st.form("my_form"):
    text = st.text_area("Enter text:", "cuántas ciudades tiene la provincia de tucuman?")
    submitted = st.form_submit_button("Submit")
    if not openai_api_key:
        st.info("Please add your OpenAI API key to continue.")
    elif submitted:
        generate_response(text)
