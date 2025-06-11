import streamlit as st
import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage

# .envの読み込み
load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

# LLMの初期化
llm = ChatOpenAI(model="gpt-3.5-turbo", openai_api_key=openai_api_key)

# ページのタイトルと説明
st.title("専門家に質問できるLLMアプリ")
st.write("下のフォームから質問を入力し、専門家の種類を選んでください。")

# ラジオボタンで専門家の種類を選択
role = st.radio(
    "専門家の種類を選んでください：",
    ("医者", "料理人", "歴史学者")
)

# 入力フォーム
user_input = st.text_input("質問を入力してください：")

# 回答を取得する関数
def get_response(role, question):
    if role == "医者":
        system_prompt = "あなたは親切で丁寧な医者として回答してください。"
    elif role == "料理人":
        system_prompt = "あなたはプロの料理人として料理のアドバイスをしてください。"
    elif role == "歴史学者":
        system_prompt = "あなたは歴史に詳しい学者として専門的に説明してください。"
    else:
        system_prompt = "あなたは優秀なアシスタントとして答えてください。"

    messages = [
        SystemMessage(content=system_prompt),
        HumanMessage(content=question)
    ]
    response = llm.invoke(messages)
    return response.content

# 入力があるときに応答を表示
if user_input:
    answer = get_response(role, user_input)
    st.write("### 回答：")
    st.write(answer)