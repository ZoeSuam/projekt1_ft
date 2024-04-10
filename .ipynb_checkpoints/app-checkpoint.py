import streamlit as st
from langchain.prompts import PromptTemplate
from langchain.llms import CTransformers



##Function to get response from llama-2-model
def getLlamaRes(input_text, num_words, answer_style):
    ## LLama2 Model
    llm = CTransformers(model='Models/llama-2-7b-chat.ggmlv3.q8_0.bin',
                        model_type='llama',
                        )
    ##Prompt Template
    template = f"""
     Answer following question but  give me a {answer_style} : {input_text} within {num_words} words"""

    prompt = PromptTemplate(input_variables=["style", "answer,", "num_words"],
                            template=template)

    ##generate response
    response = llm(prompt.format(style=answer_style,text=input_text, n_words=num_words))
    print(response)
    return response



st.set_page_config(page_title="MyFirstTry",
                   page_icon=':random:',
                   layout="centered",
                   initial_sidebar_state="collapsed")
st.header("generate Tipps")

input_text = st.text_input("Enter your Question:")

##creating two more columns
col1, col2 = st.columns([5, 5])
with col1:
    num_words = st.text_input("Number of Words to Generate")
with col2:
    answer_style = st.selectbox("how should the question get answered ", ("hint", "full solution"), index=0)

submit_button = st.button("Generate")

##Final response

if submit_button:
    st.write(getLlamaRes(input_text, num_words, answer_style))
