import streamlit as st
from groq import Groq
from dotenv import load_dotenv
import os

st.set_page_config(
    page_title="Suporte Técnico", 
    page_icon="🛠️", 
    layout="wide", 
    initial_sidebar_state="auto",
menu_items={
        'Get Help': 'https://wa.me/5531984798802',
        'Report a bug': "https://wa.me/5531984798802",
        'About': "# Um chatbot de suporte técnico de TI que responde dúvidas comuns de computador, internet e programas de forma simples e sem tecniquês — pensado para pessoas com pouca familiaridade com tecnologia."
    }
)

load_dotenv()


modelo_ia = Groq(api_key=os.getenv("GROQ_API_KEY"))

st.markdown("<h1 style='color: #722F37;'>Suporte Técnico</h1>", unsafe_allow_html=True)

if not "lista_mensagens" in st.session_state:
    st.session_state["lista_mensagens"] = [
    {"role": "system",
    "content": """Você é um assistente de suporte técnico de TI, especializado em ajudar pessoas com problemas comuns de computador, internet e programas. Responda de forma clara, simples e em passos numerados, sem usar termos muito técnicos.

Se o usuário fizer uma pergunta que NÃO seja sobre TI, suporte técnico ou tecnologia:
1. Responda de forma breve e superficial, mostrando que você entende do assunto, mas sem se aprofundar.
2. Deixe claro, de forma simpática, que esse não é seu foco principal.
3. Direcione a conversa de volta para suporte técnico, perguntando se a pessoa tem alguma dúvida nessa área.

Exemplo:
Pergunta: "Qual a capital da França?"
Resposta: "A capital da França é Paris! 🗼 Mas meu forte mesmo é ajudar com TI e suporte técnico — se tiver alguma dúvida de computador, internet ou programas, pode perguntar!"

Nunca seja rude ou recuse completamente responder — apenas mantenha o foco principal em suporte técnico."""}
]
texto_usuario = st.chat_input("Digite sua mensagem aqui...")

for mensagem in st.session_state["lista_mensagens"]:
    if mensagem["role"] != "system":
        role = mensagem["role"]
        content = mensagem["content"]
        st.chat_message(role, avatar="🛠️" if role == "assistant" else "🕵️").write(content)

if texto_usuario:
    st.chat_message("User", avatar="🕵️").write(texto_usuario)
    mensagem_usuario = {"role": "user", "content": texto_usuario}
    st.session_state.lista_mensagens.append(mensagem_usuario)

    try:
        resposta_ia = modelo_ia.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=st.session_state["lista_mensagens"]
        )
        texto_reposta_ia = resposta_ia.choices[0].message.content
    except Exception as e:
        texto_reposta_ia = "Desculpe, estou com dificuldades técnicas no momento. Tente novamente em instantes."

    st.chat_message("assistant", avatar="🛠️").write(texto_reposta_ia)
    mensagem_ia = {"role": "assistant", "content": texto_reposta_ia}
    st.session_state.lista_mensagens.append(mensagem_ia)

print(st.session_state["lista_mensagens"])

