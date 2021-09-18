
import streamlit as st
import pandas as pd

st.title("this is the title")
st.header("this the header")
st.subheader("this a subheader")

"""
# header
## subheader
"""
st.title('Portfolio Management Dashboard')

ticker = ('BTC-USD', 'ETH-USD')

dropdown = st.multiselect('Pick your assets', ticker)

start = st.date_input('Start', value= pd.to_datetime('2021-09-09'))
end = st.date_input('End', value= pd.to_datetime('today'))

if len(dropdown) > 0:
    df = yf.download(dropdown, start, end)['Adlj Close']
    st.line_chart(df)

