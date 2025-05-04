import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Set page title
st.title("World Happiness Report Dashboard")

# Load data
df = pd.read_csv('2019.csv')

# Sidebar for user input
st.sidebar.header("Filter Options")
selected_country = st.sidebar.selectbox("Select Country", df['Country or region'].unique())

# Display dataset
st.header("Dataset Preview")
st.write(df.head())

# Filter data based on selection
filtered_df = df[df['Country or region'] == selected_country]
st.header(f"Happiness Metrics for {selected_country}")
st.write(filtered_df)

# Display saved plots
st.header("Exploratory Data Analysis")

# Correlation Matrix
st.subheader("Correlation Matrix")
st.image('correlation_matrix.png')

# Happiness Distribution
st.subheader("Distribution of Happiness Scores")
st.image('happiness_distribution.png')

# Interactive Plots
st.subheader("Top 10 Happiest Countries")
with open('top_10_happiest.html', 'r', encoding='utf-8') as f:
    st.components.v1.html(f.read(), height=400)

st.subheader("GDP vs Happiness Score")
with open('gdp_vs_happiness.html', 'r', encoding='utf-8') as f:
    st.components.v1.html(f.read(), height=400)

# Dynamic Plot: Happiness Score by Region
st.subheader("Happiness Score by Region")
fig = px.box(df, x='Country or region', y='Score', title="Happiness Score by Region")
st.plotly_chart(fig)