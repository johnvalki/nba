import streamlit as st


page1 = st.page("main1.py")
page2 = st.page("main2.py")
pages = [page1,page2]
nav = st.navigation(pages)
nav.run()