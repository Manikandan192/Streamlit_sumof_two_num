import streamlit as st
st.title("Hello google")

age = st.slider("How old are you?", 0, 130, 25)
st.write("I'm ", age, "years old")

brthr_age = st.slider("How old is your brother?", 0, 130, 35)
st.write("My brother's is", age, "years old")

c= age+brthr_age
st.write("sum of age is",c)