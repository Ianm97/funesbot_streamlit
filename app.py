import streamlit as st
import numpy as np
import pandas as pd
import requests


url='http://127.0.0.1:8000/predict'

query_user_initial= st.text_input('Could you write your question? (in English please)')


params= {'user_query':query_user_initial
         }

botton_start=st.button('Submit')
if botton_start is True:
    response=requests.get(url=url,params=params).json()

    response['answer_query']['Respuesta']['content']
