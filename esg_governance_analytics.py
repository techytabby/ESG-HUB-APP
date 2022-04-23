
import altair as alt #barcharts library
import streamlit as st
import pandas as pd
import json
import requests
from st_aggrid import AgGrid
import plotly.graph_objects as go


def activfunc():


#Firebase cloud database that contains LA county income level changes within a 15 year period
    df =pd.read_json('https://esg-social-default-rtdb.firebaseio.com/.json', orient = 'records')
    
    #converts unemployed field to float values
    df['2010'] = pd.to_numeric(df['2010'], errors='coerce')
    data = df
    
    #subheader text
    st.subheader('Los Angeles County Median Income 2010 - 2020', anchor=None)
    
    #Uses streamlit-agrid to display .json dataframe chart
    AgGrid(data, height=260, ft_columns_on_grid_load=True)
    
    st.text('% percentage Diff 2010 --> 2020')
    
    st.text('White: +27.7')
    st.text('Black or African American: +21.8')
    st.text('American Indian and Alaska Native: +31.7')
    st.text('Asian: +29.3')
    st.text('Native Hawaiian or Pacific Islander: +30.5')
    st.text('Hispanic or Latino: +33')
    st.text('--------------------------------------------------------')

    #dataset set up for piechart illustration
    races = ['White', 'African American', 'American Indian/Alaskan Native', 'Asian', 'Hawaiia/Pac. Isl', 'Hispanic/Latino']
    salary = [79027, 51259, 62427, 83252, 78831, 59837]
    #Plot PieChart with plotly
    fig = go.Figure(go.Pie(labels = races, values = salary))
    st.subheader("Highest Median Income by Percentage (%)")
    st.plotly_chart(fig)
    #end of pie-chart
    
    #sub-header
    st.subheader('Median Home Sales (2020-2021) and Homeless Count', anchor=None)
    #2021 and 2022 Median home price in los angeles communities
    city_stats = pd.DataFrame({
        'city': ["Acton", "Alhambra","BaldwinPark","Cerritos", "Claremont", "Compton", "El Monte", "Inglewood"],
        '2020':[804500, 691500, 505000, 752000, 780000, 482500, 525000, 621000], 
        '2021':[844500, 700000,517500, 923500,  835000, 566000, 599500, 700000],
        'Homeless': [0, 46, 556, 46, 17, 652, 433, 525]})
    #displays dataframe of info above
    st.dataframe(city_stats)
    
   
    #data collected from: http://www.laalmanac.com/social/so14b.php
   

    
  
    
    
    
    