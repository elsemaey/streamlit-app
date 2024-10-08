import streamlit as st

st.set_page_config(
    page_title="Streamlit course",
    page_icon="rocket",
)
#st.write("# :rocket: Welcome to Streamlit Tutorial!")  # Rocket icon
st.write("# :books: Welcome to Streamlit Tutorial!")   # Books icon
#st.write("# :computer: Welcome to Streamlit Tutorial!") # Computer icon
st.sidebar.success("Select a demo above.")


st.markdown(
    """
    Streamlit is an open-source app framework for Machine Learning and Data Science. 
    It helps you create and share beautiful, custom visualizations in a few lines of code.
    **��� Select a demo from the sidebar** to see some examples
    of what Streamlit can do!
    ### Want to learn more?
    - Check out [streamlit.io](XXXXXXXXXXXXXXXXXXXX)
    - Jump into our [documentation](XXXXXXXXXXXXXXXXXXXXXXXXX)
    - Ask a question in our [community
        forums](XXXXXXXXXXXXXXXXXXXXXXXXXXXX)
    ### See more complex demos
    - Use a neural net to [analyze the Udacity Self-driving Car Image
        Dataset](XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX)
    - Explore a [New York City rideshare dataset](XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX)
"""
)