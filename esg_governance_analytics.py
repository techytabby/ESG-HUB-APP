
import altair as alt #barcharts library
import streamlit as st
import pandas as pd
import json
import requests
from st_aggrid import AgGrid


def activfunc():
#Firebase cloud database that contains employment stats per county by state
    df =pd.read_json('https://esg-social-default-rtdb.firebaseio.com/-N-uxrmkYojTDHj9Yswk.json', orient = 'records')
    #converts unemployed field to float values
    #df['Unemployed'] = pd.to_numeric(df['Unemployed'], errors='coerce')
    #Uses streamlit-agrid to display .json dataframe chart
    AgGrid(df, height=400,ft_columns_on_grid_load=True)










