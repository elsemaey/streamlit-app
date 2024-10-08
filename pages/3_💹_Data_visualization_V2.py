import streamlit as st 
import pandas as pd
import plotly.express as px
import numpy as np

@st.cache_data
def load_data(file):
    if file.type == "text/csv":
        return pd.read_csv(file)
    st.error("Unsupported file format")
    return None

def display_dataframe(df, n_rows, columns_to_show):
    st.dataframe(df.loc[:n_rows-1, columns_to_show])

def create_scatter_plot(df, x_column, y_column, color):
    return px.scatter(df, x=x_column, y=y_column, color=color)

def create_histogram(df, feature):
    return px.histogram(df, x=feature)

def create_line_plot(df, x_column, y_column, color):
    return px.line(df, x=x_column, y=y_column, color=color)

def main():
    st.title("Data Visualization App")

    file = st.file_uploader("Upload a file", type=["csv", "txt"])
    if file is None:
        st.warning("Please upload a file to continue.")
        return

    df = load_data(file)
    if df is None:
        return

    numerical_columns = df.select_dtypes(include=np.number).columns

    n_rows = st.slider("Select number of rows to display", min_value=1, max_value=100, value=5)
    # Add multiselect for columns_to_show
    columns_to_show = st.multiselect("Select columns to display", options=df.columns.tolist(), default=df.columns[:5].tolist())

    display_dataframe(df, n_rows, columns_to_show)

    tab1, tab2, tab3, tab4 = st.tabs(["Scatter Plot", "Histogram", "Line Plot", "Dataframe details"])

    with tab1:
        col1, col2, col3 = st.columns(3)
        x_column = col1.selectbox("Select the x-axis column", options=numerical_columns)
        y_column = col2.selectbox("Select the y-axis column", options=numerical_columns)
        color = col3.selectbox("Select the color column", options=df.columns)
        fig_scatter = create_scatter_plot(df, x_column, y_column, color)
        st.plotly_chart(fig_scatter)

    with tab2:
        histogram_feature = st.selectbox("Select a feature", options=numerical_columns)
        fig_hist = create_histogram(df, histogram_feature)
        st.plotly_chart(fig_hist)
    
    with tab3:
        col1, col2, col3 = st.columns(3)
        x_column = col1.selectbox("Select the x-axis column for line plot", options=numerical_columns)
        y_column = col2.selectbox("Select the y-axis column for line plot", options=numerical_columns)
        color = col3.selectbox("Select the color column for line plot", options=df.columns)
        fig_line = create_line_plot(df, x_column, y_column, color)
        st.plotly_chart(fig_line)

    with tab4:
        st.subheader("Dataframe details")
        st.write(df.describe())

if __name__ == "__main__":
    main()
