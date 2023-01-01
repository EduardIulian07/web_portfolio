import streamlit as st
from send_email import send_email

st.title("Contact me")

with st.form(key="email_form"):
    usr_email = st.text_input("Enter your email:")
    usr_choise = st.selectbox("Choose the topic of the discussion:", ["Topic1", "Topic2", "Topic3", "Topic4"])
    usr_message = st.text_area("Enter your message:")
    final_usr_message = f"""\
Subject:{usr_choise}

{usr_message}

From: {usr_email}.
"""
    submit_button = st.form_submit_button("Submit")
    if submit_button:
        send_email(usr_email, final_usr_message)
        st.info("The email was sent succesfully.", icon="✅")