import streamlit as st
st.set_page_config(page_title="Home")
page1 = st.Page("main1.py",title="nba teams comparison")
page2 = st.Page("main2.py",title="NBA teams comparison")
pages = [page1,page2]
nav = st.navigation(pages,position='top')
nav.run()