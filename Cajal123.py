import numpy as np
import pandas as pd
import streamlit as st

st.title("Welcome Everyone we are learning Python")
st.write("Python Requires Practice!!!")

data = pd.DataFrame({'c1': [23, 45, 67, 54],
                     'c2': ['A', 'B', 'C', 'D']})

st.write("Below is the table for data:")
st.write(data)

chart_data=pd.DataFrame(np.random.randn(20,3), columns=['A', 'B', 'C'])
st.line_chart(chart_data)
st.bar_chart(chart_data)
st.area_chart(chart_data)
