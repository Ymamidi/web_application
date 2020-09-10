import streamlit as st
import pandas as pd

st.title('My first app')
x= st.slider('x')
st.write(x, 'squared is', x*x)
st.write("Here's our first attempt at using data to create a table:")

st.write(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
}))

st.write(pd.read_csv (r'C:\Personal Projects\Development\Web_app\web_application\genedata-transposed.csv'))


