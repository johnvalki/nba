import streamlit as st
def newpage():
    st.header("this is a function")
st.set_page_config(page_title="Home")
page1 = st.Page("pages/main1.py",title="something")
page2 = st.Page("main2.py",title="NBA teams comparison")
pages = [page1,page2]
page3 = st.Page(newpage,title="function page")
nav = st.navigation(pages,position='top')
nav.run()