import streamlit as st
import pandas as pd
import numpy as np

#title
st.title("hello streamlit")
#paragraph
st.write("this is a simple text")

#dataframe
df = pd.DataFrame({
    'firstCol' : [1,2,3,4],
    'secondCol' : [5,6,7,8]
}) 

#display dataFrame
st.write("here is the Dataframe")
st.write(df)

#display chart
chart_data = pd.DataFrame(np.random.randn(20,3), columns=['a','b','c'])

st.line_chart(chart_data)