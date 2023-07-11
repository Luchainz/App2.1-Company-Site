import streamlit as st
from send_email import send_email

with st.form(key='email_forms'):
    user_email = st.text_input("Your email address")
    user_topic = st.text_input("What topic do you want to discuss?")
    user_message = st.text_area("Your Message")
    message = f"""
Subject: New mail from {user_email} 

From: {user_email}
{user_topic}
{user_message}
"""
    button = st.form_submit_button("Submit")
    print (button)
    if button:
        send_email(message)
        st.info("Your email was sent successfully!")