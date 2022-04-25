'''
Group: Tabetha Pombo, Arushi Nigam, and Erika Gaebel
Date: April 25, 2022
Project: DSCI 551
File: esg_events.py

Description: RSS feed that displays all the international events that are occurring that are ESG related. 
'''
#Required libraries to run this application
import feedparser
import streamlit as st

#execution function to run the application
def activfunc():
    #displays the header image
    st.image("images/events_logo.png")
    # collects rss feeds from all three below link sources
    rss_feeds = [
        'https://esgnews.com/events/feed/',
        'https://www.rallylist.com/feed/',
        'https://www.theactivistcalendar.com/events/feed/',
        'https://volunteer.extinctionrebellion.uk/rss/all/'
    ]

    
    # feeds into a list
    feeds = []
    # parses url feeds
    for url in rss_feeds:
        feeds.append(feedparser.parse(url))

    # displays rss post entries by title and link
    for feed in feeds:
        for post in feed.entries:
            st.subheader(post.title)
            st.write(post.link)
            st.write('\n--------------------------\n')