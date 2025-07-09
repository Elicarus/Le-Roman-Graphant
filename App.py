import streamlit as st
import os

@st.cache_resource
def get_file() : 
    return open("Roman Graphant.zip", 'rb')

f = get_file()
st.write("Bon ça marche que sur windows mais tkt")
st.download_button("Roman Graphant.zip", data=f, file_name="Roman Graphant.zip", on_click=lambda : st.markdown("et PAF allez tu mdis si c'est bien <a href='mailto:tomwainstain@gmail.com'>ici</a>", unsafe_allow_html=True))
