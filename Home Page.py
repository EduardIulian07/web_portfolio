import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")
col1, col2 = st.columns(2)

data_frame = pd.read_csv("data.csv", sep=";")

with col1:
    st.image("images/me.png")
    

with col2:
    st.title("ATODIRESEI Eduard Iulian")
    description = """
    Hello! I'm Eduard and I am a second year student a University Politehnica of Bucharest at the Faculty of electronics
    and I am very passionate about everything that includes technology. Currently I am working with my team , "FunkyBits", 
    on a project of building a fully autonomous 1:10 scale vehicle that is supposed to behave just like in a real-life 
    case scenario.
    """
    st.info(description)

content = """
Below you can find some of the apps I developed in python. Feel free to contact me!
"""

st.write(content)

col3, middle_col, col4 = st.columns([1.5, 0.5, 1.5])

with col3:
    for index, row in data_frame.iterrows():
        if index%2 == 0:
            st.header(str(index+1) + ". " + row["title"])
            app_content = row["description"]
            st.info(app_content)
            st.image("images/" + row["image"], width=250)
            st.write(f"[Source code]({row['url']})")


with col4:
    for index, row in data_frame.iterrows():
        if index%2 == 1:
            st.header(str(index+1) + ". " + row["title"])
            app_content = row["description"]
            st.info(app_content)
            st.image("images/" + row["image"], width=250)
            st.write(f"[Source code]({row['url']})")