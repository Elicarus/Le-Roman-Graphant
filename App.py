import streamlit as st
import os

@st.cache_resource
def get_file() : 
    return open(os.path.join("final version", "Roman Graphant.zip"), 'rb')

f = get_file()
st.download_button("Roman Graphant.zip", data=f, file_name="Roman Graphant.zip", on_click=lambda : st.write("Have fun!!"))
