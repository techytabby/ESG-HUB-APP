'''
Group: Tabetha Pombo, Arushi Nigam, and Erika Gaebel
Date: April 25, 2022
Project: DSCI 551
File: esg_analytics.py
This page contains the navigation structure of the analytics page. The radio navigation controls the proper analytic category that will display
'''
#required libraries for app to function
import streamlit as st
import plotly.express as px
import pandas as pd
import esg_environmental_analytics
import esg_governance_analytics
import esg_social_analytics

#actifunc that controls the execution of the app
def activfunc():
    #displays the radio navigation
    genre = st.radio(
        "Choose a below category For analytic data:",
        ('Environmental', 'Social', 'Governance'))
    #if 'Environmental' is selected execute esg_environmental_analytics.py app
    if genre == 'Environmental':
        esg_environmental_analytics.activfunc()
    # if 'Social' is selected execute esg_social_analytics.app    
    elif genre == 'Social':
        esg_social_analytics.activfunc()
    #if 'Governance' is selected execute esg_governance_analytics.py file    
    elif genre == 'Governance':
        esg_governance_analytics.activfunc()
    else:
        #displays for user to choose category
        st.write("Choose an Option")