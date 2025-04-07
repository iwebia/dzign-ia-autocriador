import streamlit as st
import openai
import os

st.set_page_config(page_title="DZIGN IA CREATOR™", layout="centered")
st.title("🚀 DZIGN IA CREATOR™ - AutoCriação Inteligente")
st.subheader("Descreva sua IA e gere o código automaticamente com GPT-4.")

openai.api_key = os.getenv("OPENAI_API_KEY")

briefing = st.text_area("✍️ Qual IA você deseja criar? (Ex: IA para vídeos motivacionais no Instagram)", height=150)

if st.button("Gerar Código da IA"):
    with st.spinner("💡 Gerando código com GPT..."):
        prompt = f"""
        Gere um código Python modular para uma IA com as seguintes características:
        {briefing}
        O código deve conter:
        - Geração de roteiro com GPT
        - Narração com ElevenLabs
        - Placeholder de imagem
        - Montagem com MoviePy
        """
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "Você é uma engenheira de software especializada em IA."},
                {"role": "user", "content": prompt}
            ]
        )
        codigo = response["choices"][0]["message"]["content"]
        st.code(codigo, language="python")
        st.success("✅ Código gerado com sucesso!")

