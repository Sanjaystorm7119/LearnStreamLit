import streamlit as st
import pandas as pd

#title
st.title("Streamlit Input box")

#inputbox
name = st.text_input("enter your name")

#printname
if name:
    st.write(f"hello {name}")

# slider
age = st.slider("select your age",0,100,18)  #label is a must (start , end , default)
st.write(f"your age is {age}")

#select box

options = ["python" , "Ai" , "Ml" , "Ds"]
choice = st.selectbox("choose" , options)
st.write(f"you selected {choice}")

data = {
    "name" : ["san", "jay"],
    "age" : [10,20],
    "city" : ["chennai" , "pune"]
}
df = pd.DataFrame(data)
df.to_csv("samplecsv.csv")

st.table(df) 
#static , Renders the DataFrame as a non-interactive table. 
# No sorting, scrolling, or column resizing.

st.write(df) 
"""
Renders as an interactive table:
You can sort columns.
Can scroll if the table is large.
Better for large datasets or when user interaction is helpful.
"""

upload_files = st.file_uploader("choose a file type" , type="csv")
#single type

upload_files1 = st.file_uploader("choose a file type" , type=["csv", "xlsx", "txt"])
#multiple types

if upload_files1 is not None:
    # df=pd.read_csv(upload_files)
    df=pd.read_csv(upload_files1)
    st.write(df)


##check streamlit.io


