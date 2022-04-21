import altair as alt
import pandas as pd
import streamlit as st


def activfunc():
    #import .csv data from fortune-500-diversity dataset into a dataframe using pandas
    industry_data = pd.read_csv('data/race_industry.csv')
    #prints out df records

    st.subheader("Employee Counts Per Industry / Race Category")
    df = pd.DataFrame(industry_data)

    st.write(df)
    #chart
    a_bar = alt.Chart(industry_data).mark_bar().encode(x='Caucasian_Total:Q', y='Industry:O', opacity=alt.value(0.6),color=alt.value('blue')).properties(width=800, height=300)
    b_bar = alt.Chart(industry_data).mark_bar().encode(x='AfricanAmerican_Total:Q', y='Industry:O', opacity = alt.value(0.8),color=alt.value('orange')).properties(width=800,height=300)
    c_bar = alt.Chart(industry_data).mark_bar().encode(x='Asian_Total:Q', y='Industry:O' , opacity = alt.value(0.4),color=alt.value('green')).properties(width=800, height=300)

    #displays layered chart total employees per industry
    st.altair_chart(a_bar + b_bar + c_bar)

    #management chart per race
    d_bar = alt.Chart(industry_data).mark_bar().encode(x='Caucasian_Management:Q', y='Industry:O', opacity=alt.value(0.6), color=alt.value('blue')).properties(width=800, height=300)
    e_bar = alt.Chart(industry_data).mark_bar().encode(x='AfricanAmerican_Management:Q', y='Industry:O', opacity=alt.value(0.8), color=alt.value('orange')).properties(width=800, height=300)
    f_bar = alt.Chart(industry_data).mark_bar().encode(x='Asian_Management:Q', y='Industry:O', opacity=alt.value(0.4), color=alt.value('green')).properties(width=800, height=400)
    st.altair_chart(d_bar + e_bar + f_bar)

    #source=industry_data()
    #b_bar = alt.Chart(source).mark_bar(opacity=0.7).encode( x ='Caucasian_Total:0', y=alt.Y('Industry:Q', stack=None), color=not "source")
    #st.altair_chart(b_bar)
