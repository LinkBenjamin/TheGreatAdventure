#!/usr/bin/env python
# coding: utf-8

import streamlit as st # import the Streamlit library
from langchain.chains import LLMChain, SimpleSequentialChain # import LangChain libraries
from langchain.llms import OpenAI # import OpenAI model
from langchain.prompts import PromptTemplate # import PromptTemplate
# from langchain.memory import ChatMessageHistory
# from langchain.memory import ConversationBufferMemory
import prompt
import helper
import constants as constants
import openai

# history = ChatMessageHistory()
helper.add_logo()
openai_api_key = constants.OPEN_API_KEY

llm = OpenAI(temperature=0.7, openai_api_key=openai_api_key)


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
    prompt_template = PromptTemplate(input_variables=["name", "age", "interests", "topic"], template=template)
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
    ####### BEGIN IMAGE CODE #######
    openai.api_key = openai_api_key
    response = openai.Image.create(
        prompt=summary,
        n=1,
        size="512x512",
    )
    
    imageUrl = response["data"][0]["url"]


    st.markdown(f"![Alt Text]({imageUrl})")
    ####### END IMAGE CODE #######


