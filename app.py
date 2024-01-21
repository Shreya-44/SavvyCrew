import streamlit as st
import pandas as pd
from pandasai import Agent
from pandasai import SmartDataframe
from pandasai.llm.openai import OpenAI

def initialize_smart_dataframe():
    llm = OpenAI(api_token="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", temperature=0, model="gpt-3.5-turbo-0613")
    return SmartDataframe("CO2 Emissions_Canada.csv", config={"llm": llm})

def get_chat_response(question, dataframe):
    return dataframe.chat(question)

def main():
    st.title("Climate Tech Chatbot")

    smart_df = initialize_smart_dataframe()

    chat_history=[]

    user_input = st.text_input("You: ")

    if st.button("Ask"):
        if user_input:
            response = get_chat_response(user_input, smart_df)
            chat_history.append(("You", user_input))
            chat_history.append(("Bot", response))
            st.write(response)

    for sender, message in chat_history:
        st.text(f"{sender}: {message}")

if __name__ == "__main__":
    main()
