import streamlit as st
import pandas

data = {
    'Series_1': [1,3,4,5,7],
    'Series_2': [10,30,40,100,250]
}

df = pandas.DataFrame(data)

st.title('Our First Stramlit App')
st.subheader('Intorducing Streamlit in Automate Everything with Python')
st.write('''This is our first Web App. Enjoy it!''')
st.write(df)
st.line_chart(df)
st.area_chart(df)

myslider = st.slider('Celsius')
st.write(myslider, 'in Fahrenheit is', myslider * 9/5)