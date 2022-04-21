import streamlit as st
import pprint
import requests
import pandas as pd
import numpy as np


def activfunc():
    st.title('News')

    url = 'https://gnews.io/api/v4/search?q=esg&lang=en&token=619cdfe716bdcf9f981367c9d6e62625'
    response = requests.get(url)
    response_json = response.json()

    for i in response_json['articles']:
        st.subheader(i['title'])
        st.write(i['url'])
        st.write(i['description'])
    pprint.pprint(response_json)