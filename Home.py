import streamlit as st
import numpy as np
import pandas as pd
from crawl_url import crawl_url
from model import GeneralModel



'# MyThorch'

pred = GeneralModel()

api_key = st.text_input("OpenAI API Key", "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")

@st.cache_data
def process_prompt(input):
    return pred.model_prediction(input=crawl_url(input) , api_key=api_key)

if api_key:

    # # Setting up the Title
    # st.title("Write a poem based on these words")

    # # st.write("---")

    # s_example = "Birds, flowers, love, sun"
    # input = st.text_area(
    #     "Use the example below or input your own text in English",
    #     value=s_example,
    #     max_chars=150,
    #     height=100,
    # )
    input = st.text_input("Document URL")

    if st.button("Submit"):
        with st.spinner(text="In progress"):
            report_text = process_prompt(input)
            st.write(report_text[0])
            st.text(report_text[1])
else:
    st.error("🔑 Please enter API Key")