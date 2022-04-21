import feedparser
import streamlit as st


def activfunc():
    st.image("images/events_logo.png")
    # collects rss feeds
    rss_feeds = [
        'https://esgnews.com/events/feed/',
        'https://www.rallylist.com/feed/',
        'https://www.theactivistcalendar.com/events/feed/',
        'https://volunteer.extinctionrebellion.uk/rss/all/'
    ]

    # streamlit title

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