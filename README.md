# 🛠️ Suporte Técnico Automatizado

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://suportetecnico.streamlit.app)
![Python](https://img.shields.io/badge/Python-3.x-blue)
![Status](https://img.shields.io/badge/status-online-brightgreen)

Um chatbot de suporte técnico de TI que responde dúvidas comuns de computador, internet e programas de forma simples e sem "tecniquês" — pensado para pessoas com pouca familiaridade com tecnologia.

**🔗 Acesse agora:** [suportetecnico.streamlit.app](https://suportetecnico.streamlit.app)

---

## 📋 Sobre o projeto

Esse projeto nasceu da ideia de aproximar suporte técnico de quem mais precisa dele, mas costuma se sentir intimidado por termos técnicos. O assistente foi configurado com um prompt de sistema específico para responder de forma clara, em passos numerados, evitando jargão técnico sempre que possível.

Foi desenvolvido como parte do meu processo de transição de carreira para a área de tecnologia, aplicando conceitos de integração com APIs de IA generativa, boas práticas de segurança (variáveis de ambiente) e deploy em produção.

## ✨ O que ele faz

- 💬 Responde perguntas sobre problemas comuns de computador, internet e programas
- 📶 Ajuda com troubleshooting básico (Wi-Fi, lentidão, erros de programas, etc.)
- 🗣️ Explica soluções em linguagem simples, passo a passo
- 🔁 Mantém o histórico da conversa durante a sessão

### Exemplos de perguntas que você pode fazer:
- "Meu Wi-Fi caiu, o que eu faço?"
- "Meu computador está muito lento, como resolver?"
- "Não consigo abrir um arquivo PDF, o que pode ser?"
- "Como eu libero espaço no meu computador?"

## 🧰 Tecnologias utilizadas

- **[Streamlit](https://streamlit.io/)** — interface web interativa
- **[Groq API](https://groq.com/)** — modelo de linguagem (Llama 3.3 70B) para geração das respostas
- **python-dotenv** — gerenciamento seguro de variáveis de ambiente
- **Streamlit Community Cloud** — hospedagem e deploy

## 🔒 Segurança

A chave de API (`GROQ_API_KEY`) é mantida fora do código-fonte, protegida via arquivo `.env` local (listado no `.gitignore`) e configurada como *Secret* diretamente na plataforma de deploy — nunca exposta publicamente no repositório.

## 🚀 Como rodar localmente

```bash
# Clone o repositório
git clone https://github.com/oDevMarques/suporte-tecnico-automatizado.git
cd suporte-tecnico-automatizado

# Instale as dependências
pip install -r requirements.txt

# Crie um arquivo .env na raiz do projeto com sua chave da Groq
echo "GROQ_API_KEY=sua_chave_aqui" > .env

# Execute a aplicação
streamlit run main.py
```

## 📂 Estrutura do projeto

```
suporte-tecnico-automatizado/
├── main.py              # Aplicação principal (interface + lógica do chatbot)
├── requirements.txt      # Dependências do projeto
├── .env                  # Variáveis de ambiente (não versionado)
├── .gitignore
└── README.md
```

## 👨‍💻 Autor

**Anthony Marques Barreto**

Em transição de carreira para desenvolvimento de software, com foco em Java e experiência prévia em suporte de TI e gestão de operações.

- GitHub: [@oDevMarques](https://github.com/oDevMarques)
- LinkedIn: https://www.linkedin.com/in/anthony-marques-2145771b9/
---

⭐ Se esse projeto foi útil ou interessante pra você, considere deixar uma estrela no repositório!
