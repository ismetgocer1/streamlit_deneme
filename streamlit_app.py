import streamlit as st
import pandas as pd
import numpy as np

# Sample data for bar chart
bar_data = {
    'Category': ['A', 'B', 'C', 'D', 'E'],
    'Values': [25, 40, 10, 30, 15]
}

st.title("Simple Data Visualization")

# Bar Chart
st.subheader("Bar Chart Example")  # 1. grafik
bar_df = pd.DataFrame(bar_data)
st.bar_chart(bar_df.set_index('Category'))

# Line Chart
st.subheader("Line Chart Example")  # 2. grafik

# Slider for X values
x_min = 0
x_max = 200
x_value = st.slider("Select a range for X values:", x_min, x_max, (0, 100))

# Generate data for the selected range
x = np.linspace(x_value[0], x_value[1], 100)
y = np.sin(x)

# Create a DataFrame for the line chart
line_df = pd.DataFrame({'x': x, 'y': y}).set_index('x')

# Display the line chart
st.line_chart(line_df)
