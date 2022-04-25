'''
Group: Tabetha Pombo, Arushi Nigam, and Erika Gaebel
Date: April 25, 2022
Project: DSCI 551
File: news.py

Description: This displays esg news related articles from gnew.io api connector.
'''
#Required Libraries to run app
import streamlit as st
import pprint
import requests
import pandas as pd
import numpy as np
#executes initial function for the web app to work
def activfunc():
    st.title('News')
    #GNews.io API connector with privatekey access token
    url = 'https://gnews.io/api/v4/search?q=esg&lang=en&token=619cdfe716bdcf9f981367c9d6e62625'
    response = requests.get(url)
    response_json = response.json()
    #displays all articles: title, url, and description
    for i in response_json['articles']:
        st.subheader(i['title'])
        st.write(i['url'])
        st.write(i['description'])
    #outputs it to the web app for user viewing    
    pprint.pprint(response_json)