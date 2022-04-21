import streamlit as st
import plotly.express as px
import pandas as pd
import esg_environmental_analytics
import esg_governance_analytics
import esg_social_analytics


def activfunc():
    genre = st.radio(
        "Choose a below category For analytic data:",
        ('Environmental', 'Social', 'Governance'))

    if genre == 'Environmental':
        esg_environmental_analytics.activfunc()
    elif genre == 'Social':
        esg_social_analytics.activfunc()
    elif genre == 'Governance':
        esg_governance_analytics.activfunc()
    else:
        st.write("Choose an Option")