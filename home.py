import streamlit as st


page1 = st.Page("main1.py")
page2 = st.Page("main2.py")
pages = [page1,page2]
nav = st.navigation(pages)
nav.run()