import streamlit as st
import numpy as np
import pandas as pd


st.title("Hey Bhoomi,Welcome from Streamlit")

st.write("This is write mehtod in streamlit")

#Create datafram

df=pd.DataFrame({
    'first column':[1,2,3],
    'second column':['a','b','c'],

})

st.write(df)

#Create Line Chart

line_chart=pd.DataFrame(
    np.random.randn(10,3),columns=['x','y','z']
)

st.line_chart(line_chart)


#interactions

age=st.text_input("Enter ur age")

if(age):
    st.write(f"So u are {age} already???")






