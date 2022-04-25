'''
Group: Tabetha Pombo, Arushi Nigam, and Erika Gaebel
Date: April 25, 2022
Project: DSCI 551
File: esg_social_analyics.py

Description: Displays employee and management level employees within each industry by race. GitHub .csv file format containing dataset was used for charts and tabular chart.
'''
#Libraries Required for App to Run
import altair as alt
import pandas as pd
import streamlit as st
#Main function that executes app
def activfunc():
    #import .csv data from fortune-500-diversity dataset into a dataframe using pandas
    industry_data = pd.read_csv('data/race_industry.csv')
    #prints out df records
    #subheader text display
    st.subheader("Employee Counts Per Industry / Race Category")
    df = pd.DataFrame(industry_data)
    #displays the tabular chart that contains the employee counts per industry/race
    st.write(df)
    #(caucasian-blue, afrian american - yellow, asian-green)
    a_bar = alt.Chart(industry_data).mark_bar().encode(x='Caucasian_Total:Q', y='Industry:O', opacity=alt.value(0.6),color=alt.value('blue')).properties(width=800, height=300)
    b_bar = alt.Chart(industry_data).mark_bar().encode(x='AfricanAmerican_Total:Q', y='Industry:O', opacity = alt.value(0.8),color=alt.value('orange')).properties(width=800,height=300)
    c_bar = alt.Chart(industry_data).mark_bar().encode(x='Asian_Total:Q', y='Industry:O' , opacity = alt.value(0.4),color=alt.value('green')).properties(width=800, height=300)

    #displays layered chart total non-managerial employees  per industry (caucasian-blue, afrian american - yellow, asian-green)
    st.altair_chart(a_bar + b_bar + c_bar)

    #management chart per race (caucasian-blue, afrian american - yellow, asian-green)
    d_bar = alt.Chart(industry_data).mark_bar().encode(x='Caucasian_Management:Q', y='Industry:O', opacity=alt.value(0.6), color=alt.value('blue')).properties(width=800, height=300)
    e_bar = alt.Chart(industry_data).mark_bar().encode(x='AfricanAmerican_Management:Q', y='Industry:O', opacity=alt.value(0.8), color=alt.value('orange')).properties(width=800, height=300)
    f_bar = alt.Chart(industry_data).mark_bar().encode(x='Asian_Management:Q', y='Industry:O', opacity=alt.value(0.4), color=alt.value('green')).properties(width=800, height=400)
    #Displays the second chart that represents manageral level employees per race and industry
    st.altair_chart(d_bar + e_bar + f_bar)
