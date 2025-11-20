import streamlit as st
st.set_page_config(page_title="Home")
page1 = st.Page("main1.py")
page2 = st.Page("main2.py")
pages = [page1,page2]
nav = st.navigation(pages)
nav.run()