import streamlit as st
import pandas as pd
data = {
    'Series_1': [1, 2, 3, 4, 5],
    'Series_2': [10, 20, 30, 40, 50]
}
df = pd.DataFrame(data)
st.title('Our First Streamlit App')
st.subheader('Introducing Streamlit in Automate Everything with python')
st.write('This is our First webapp')
st.write(df)
