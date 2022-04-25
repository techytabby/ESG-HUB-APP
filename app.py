'''
Group: Tabetha Pombo, Arushi Nigam, and Erika Gaebel
Date: April 25, 2022
Project: DSCI 551
File: app.py
This contains the home page of the project that displays the definitions of ESG. Utilizes streamlit columns to structure out invidiual image files for header and footer.
Logos are stored in the images/ folder of the project
'''
#Libraries required to run app.py script
import streamlit as st
import esg_home
import esg_news
import esg_events
import esg_analytics

# Create main side bar between categories
my_pages = st.sidebar.selectbox('Choose Your Topic:', ['Home', 'News', 'Analytics', 'Events']);
# use this CSS stylesheet
with open("stylesheet.css") as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True);

#Menu nagivation drop down for the entire web app
# if Home is clicked on, execute the following
if my_pages == 'Home':
    esg_home.activfunc()
# If News is selected in the drop-down, then navigate to the News pages
elif my_pages == 'News':
    esg_news.activfunc()
#if Analytics is selected in the drop-down, then navigate to the analytics page
elif my_pages == 'Analytics':
    esg_analytics.activfunc()
#if Events is selected in the drop down, then navigate to the events page
elif my_pages == 'Events':
    esg_events.activfunc()
#if None is selected then default page will be esg_home 'Home' page.    
else:
    esg_home;