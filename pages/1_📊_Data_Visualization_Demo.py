import streamlit as st 
import pandas as pd
import plotly.express as px
import numpy as np

@st.cache_data
def load_data(file):
    if file.type == "text/csv":
        df = pd.read_csv(file)
    else:
        st.error("Unsupported file format")
        return None
    return df
file = st.file_uploader("Upload a file", type=["csv", "txt"])

if file is not None:
    df = load_data(file)
    n_rows = st.slider("Number of rows to display", min_value=1, max_value=len(df), value=5)
    column_to_show= st.multiselect("Select columns ", options=df.columns.tolist(), default=df.columns.tolist())
    numerical_columns = df.select_dtypes(include=np.number).columns
    st.write(df[:n_rows][column_to_show])

tab1, tab2, tab3, tab4 = st.tabs(["Scatter Plot", "Histogram","Line Plot","Datafram details"])

with tab1:
#    st.subheader("Scatter Plot")
    col1, col2, col3 = st.columns(3) 
    with col1:
        x_column = st.selectbox("Select the x-axis column", options=numerical_columns)
    with col2:
        y_column = st.selectbox("Select the y-axis column", options=numerical_columns)
    with col3:
        color = st.selectbox("Select the color column", options=df.columns)
#    st.title("Scatter Plot")
    fig_scatter = px.scatter(df, x=x_column, y=y_column , color=color)
    st.plotly_chart(fig_scatter)
with tab2:
#    st.subheader("Histogram")
#    st.title("Histogram")
    histogram_feature = st.selectbox("Select a feature", options=numerical_columns)
    fig_hist = px.histogram(df, x=histogram_feature)
    st.plotly_chart(fig_hist)
    
with tab3:
    st.subheader("Line Plot")
    col1, col2 = st.columns(2)
    with col1:
#        x_column = st.selectbox("Select the x-axis column", options=df.columns)
#        y_column = st.selectbox("Select the y-axis column", options=numerical_columns)
#        color = st.selectbox("Select the color column", options=df.columns)
        fig_line = px.line(df, x=x_column, y=y_column, color=color)
        st.plotly_chart(fig_line)
#        st.title("Line Plot")
#        st.plotly_chart(fig_line)
#        st.title("Box Plot")
#        fig_box = px.box(df, y=y_column, color=color)
#        st.plotly_chart(fig_box)
with tab4:
        st.subheader("Dataframe details")
        st.write(df.describe())
