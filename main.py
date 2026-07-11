import streamlit as st
from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()


modelo_ia = Groq(api_key=os.getenv("GROQ_API_KEY"))

st.markdown("<h1 style='color: #722F37;'>Suporte Técnico</h1>", unsafe_allow_html=True)

if not "lista_mensagens" in st.session_state:
    st.session_state["lista_mensagens"] = [
    {"role": "system", "content": "Você é um assistente de suporte técnico de TI, especializado em ajudar pessoas com problemas comuns de computador, internet e programas. Responda de forma clara, simples e em passos numerados, sem usar termos muito técnicos."}
]
texto_usuario = st.chat_input("Digite sua mensagem aqui...")

for mensagem in st.session_state["lista_mensagens"]:
    if mensagem["role"] != "system":
        role = mensagem["role"]
        content = mensagem["content"]
        st.chat_message(role).write(content)

if texto_usuario:
    st.chat_message("User").write(texto_usuario)
    mensagem_usuario = {"role": "user", "content": texto_usuario}
    st.session_state.lista_mensagens.append(mensagem_usuario)

    resposta_ia = modelo_ia.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=st.session_state["lista_mensagens"]
    )
    print(resposta_ia)
    texto_reposta_ia = resposta_ia.choices[0].message.content

    st.chat_message("assistant").write(texto_reposta_ia)
    mensagem_ia = {"role": "assistant", "content": texto_reposta_ia}
    st.session_state.lista_mensagens.append(mensagem_ia)

print(st.session_state["lista_mensagens"])

