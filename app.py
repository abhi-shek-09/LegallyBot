import streamlit as st
import google.generativeai as genai
from load_creds import load_creds

creds = load_creds()

genai.configure(credentials=creds)

name = "legallybot-nmz2rvthhb9b"
model = genai.GenerativeModel(model_name=f'tunedModels/{name}')

st.title("LegallyBot ⚖️")
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("What is up?"):
    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})
    result =  model.generate_content(f'{prompt}')
    response = f"{result.text}"
    with st.chat_message("assistant"):
        st.markdown(response)
    st.session_state.messages.append({"role": "assistant", "content": response})






# result = model.generate_content('When can the Enrollment Application can be obtained from Bar Council?')
# print(result.text)