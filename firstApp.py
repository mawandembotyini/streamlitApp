import streamlit as st
import pandas as pd
from io import StringIO 

st.title('My first app on Streamlit!!!')
st.write('Wandie is a Goat')
st.write('weldone Wandie this is just the beggining')
st.write('This is nice !!!')
st.number_input('irradiance', min_value=0, max_value=1500, value=900, format=None, key=None, help=None, on_change=None)
color = st.color_picker('Pick A Color', '#00f900')
st.write('The current color is', color)

uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
     # To read file as bytes:
     bytes_data = uploaded_file.getvalue()
     st.write(bytes_data)

     # To convert to a string based IO:
     stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
     st.write(stringio)

     # To read file as string:
     string_data = stringio.read()
     st.write(string_data)

     # Can be used wherever a "file-like" object is accepted:
     dataframe = pd.read_csv(uploaded_file)
     st.write(dataframe)