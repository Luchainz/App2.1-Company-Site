import streamlit as st
import pandas

top = pandas.read_csv('topics.csv')
dat = pandas.read_csv('data1.csv')

st.set_page_config(layout='wide')
st.title("The Best company")
st.text("Lorem Ipsolum")
st.header("Our Team")

col1, col2, col3 = st.columns(3)

with col1:
    for index, row in dat[:4].iterrows():
        # st.header(f"{row['first name']} {row['last name']}")
        st.header(f"{row['first name'].capitalize()} {row['last name'].capitalize()}")
        st.write(row['role'])
        st.image("images1/" + row["image"])

with col2:
    for index, row in dat[4:8].iterrows():
        st.header(f"{row['first name'].capitalize()} {row['last name'].capitalize()}")
        st.write(row['role'])
        st.image("images1/" + row["image"])

with col3:
    for index, row in dat[8:].iterrows():
        st.header(f"{row['first name'].capitalize()} {row['last name'].capitalize()}")
        st.write(row['role'])
        st.image("images1/" + row["image"])


