'''
Group: Tabetha Pombo, Arushi Nigam, and Erika Gaebel
Date: April 25, 2022
Project: DSCI 551
File: esg_home.py
This contains the home page of the project that displays the definitions of ESG. Utilizes streamlit columns to structure out invidiual image files for header and footer.
Logos are stored in the images/ folder of the project
'''
import streamlit as st
# Homepage contains default display screen in app

def activfunc():
    # displays the banner on the homepage
    st.image("images/logo.jpeg")

    # displays icons with ESG definitions

    with st.container():
        st.subheader("Environmental")
        st.caption(
            "Environmental, involves how organizations perform as a steward of our natural environment, with a focus on: waste, pollution, resource depletion, greenhouse gas emissions, deforestation, and climate change.")
    with st.container():
        st.subheader("Social")
        st.caption(
            "How companies treat people, with a concentration on: employee relations, diversity, working conditions, serving underdeveloped communities, health/safety, and conflict.")
    with st.container():
        st.subheader("Governance")
        st.caption("Involves the criteria, which examines how corporations policy themselves - how they're governed and how they manage: tax strategies executive remuneration, donations/lobbying, corruption/bribery, and board diversity/structure.")
    # columns that contain and display the footer images of this section
    col1, col2, col3 = st.columns(3)
    with col1:
        st.write("")
    with col2:
        st.image("images/leaf_icon.png")
    with col3:
        st.write("")