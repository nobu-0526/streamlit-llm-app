from dotenv import load_dotenv
load_dotenv()

from langchain_openai import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage

llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0)

def get_response(selected_item, user_input):
    response = llm.invoke([
        SystemMessage(content=f"You are a helpful assistant for {selected_item}."),
        HumanMessage(content=user_input)
    ])
    return response

import streamlit as st
st.title("LLM App")
st.write("これはユーザーが選んだ専門家に基づいて、LLMが応答するアプリです。")
st.write("次の専門家を選んでください。1.エンジニア,2.営業担当者")
st.divider()

selected_item = st.radio(
    "専門家を選択してください",
    ["エンジニア", "営業担当者"]
) 
user_input = st.text_input("質問を入力してください")
if st.button("送信"):
    if user_input:
        response = get_response(selected_item, user_input)
        # invokeの返り値はAIMessage型なのでcontent属性でOK
        st.write("LLMの応答:", response.content)
    else:
        st.write("質問を入力してください。")