import streamlit as st
import numpy as np
st.write("""
#Maximum of 3 Numbers""")
st.header('User Input Parameters')

num1=st.number_input('Number 1')
num2=st.number_input('Number 2')
num3=st.number_input('Number 3')

x=max(num1,num2,num3)
st.header('Maximum number is: ')
st.write(x)