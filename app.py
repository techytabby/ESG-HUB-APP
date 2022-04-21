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

# if Home is clicked on, execute the following
if my_pages == 'Home':
    esg_home.activfunc()

# if Environmental is selected
elif my_pages == 'News':
    esg_news.activfunc()

elif my_pages == 'Analytics':
    esg_analytics.activfunc()

elif my_pages == 'Events':
    esg_events.activfunc()
    # if category is Analytics, execute the following
else:
    esg_home;