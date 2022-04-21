import streamlit as st
import pprint
import requests
import pandas as pd
import numpy as np
from datetime import*




#news api
url = 'https://gnews.io/api/v4/search?q=esg&lang=en&token=619cdfe716bdcf9f981367c9d6e62625'
response = requests.get(url)
response_json = response.json()

words = []

for word in response_json['articles']:
    words.append(word['title'])
print(words)
