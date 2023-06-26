#!/usr/bin/env python
# coding: utf-8

import streamlit as st # import the Streamlit library
from langchain.chains import LLMChain, SimpleSequentialChain # import LangChain libraries
from langchain.llms import OpenAI # import OpenAI model
from langchain.prompts import PromptTemplate # import PromptTemplate
# from langchain.memory import ChatMessageHistory
# from langchain.memory import ConversationBufferMemory
import prompt

# history = ChatMessageHistory()


llm = OpenAI(temperature=0.7, openai_api_key="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")


name = st.text_input(
    "Name  ",
)
age = st.text_input(
        "Age: ",
        )
interests = st.text_input(
        "Interests: "
        )
topic = st.text_input(
        "Topic: "
        )



if st.button("Tell me a story", type="primary"):


    template = prompt.prompt1
    #.format(name=name, age=age, interests=interests, topic=topic)
    print(template)
    prompt_template = PromptTemplate(input_variables=["name", "age", "interests", "topic"], template=template)
    question_chain = LLMChain(llm=llm, prompt=prompt_template)



    st.success(question_chain.run({"name":name, "age":age, "interests": interests, "topic": topic} ))
