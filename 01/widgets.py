import streamlit as st

#title
st.title("Streamlit Input box")

#inputbox
name = st.text_input("enter your name")

#printname
if name:
    st.write(f"hello {name}")