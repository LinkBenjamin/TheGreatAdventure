#!/usr/bin/env python
# coding: utf-8

import streamlit as st # import the Streamlit library
from langchain.chains import LLMChain, SimpleSequentialChain # import LangChain libraries
from langchain.llms import OpenAI # import OpenAI model
from langchain.prompts import PromptTemplate # import PromptTemplate
# from langchain.memory import ChatMessageHistory
# from langchain.memory import ConversationBufferMemory
import prompt
import os

# history = ChatMessageHistory()


llm = OpenAI(temperature=0.7, openai_api_key=os.environ['OPENAI_API_KEY'])


name = st.text_input(
    "Name  ",
)
if not os.path.isfile(f'{name}.history'):
    age = st.text_input(
            "Age: ",
            )
    interests = st.text_input(
            "Interests: "
            )
    topic = st.text_input(
            "Topic: "
            )
    extender = ''
else:
    age='same as before',
    interests = 'same as before'
    topic = 'same as before'
    with open(f'{name}.history', 'r') as f:
        extender = f.read()



if st.button("Tell me a story", type="primary"):


    template = prompt.prompt1 + extender
    prompt_template = PromptTemplate(input_variables=["name", "age", "interests", "topic"], template=template)
    if not os.path.isfile(f'{name}.history'):
        with open(f'{name}.history', 'a') as f:
            f.write(prompt.prompt1.format(name=name, age=age, interests=interests, topic=topic))
    question_chain = LLMChain(llm=llm, prompt=prompt_template)

    template = '''summarize the following in a way that can be used to prompt creation of an image::
        {statement}'''
    prompt_template = PromptTemplate(input_variables=["statement"], template=template)
    summary_chain = LLMChain(llm=llm, prompt=prompt_template)

    rslt = question_chain.run({"name":name, "age":age, "interests": interests, "topic": topic})
    with open(f'{name}.history', 'a') as f:
        f.write(rslt)
    summary = summary_chain.run({"statement": rslt})
    st.write(rslt)
    st.write(summary)


