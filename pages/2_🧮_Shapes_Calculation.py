import streamlit as st 
import  time
st.header("Shapes Calculation")

st.sidebar.header("Select Shape")

with st.sidebar:
    shape = st.selectbox("Select Shape", ["Square", "Rectangle", "Circle", "Triangle"])

if shape == "Circle":
    radius=st.number_input("Enter Radius:", min_value=0.0,max_value=100.0, step=0.1)
    area=radius * radius * 3.14
    perimeter=2*3.14*radius
if shape == "Rectangle":
    width=st.number_input("Enter Width:", min_value=0.0, max_value=100.0, step=0.1)
    hight=st.number_input("Enter Height:", min_value=0.0, max_value=100.0, step=0.1)
    area=width*hight
    perimeter=2*(width+hight) 
if shape == "Triangle":
    base=st.number_input("Enter Base:", min_value=0.0, max_value=100.0, step=0.1) 
    height=st.number_input("Enter Height:", min_value=0.0, max_value=100.0, step=0.1)
    area=0.5*base*height
    perimeter=base+height+base
if shape == "Square":
    side=st.number_input("Enter Side:", min_value=0.0, max_value=100.0, step=0.1)
    area=side*side
    perimeter=4*side
    
compute_btn=st.button("Calculate Area and perimeter ")
if compute_btn:
    st.subheader("Results")
    with st.spinner("Wait for Compute..."):
        time.sleep(2)
        st.success("Done!")
    with st.expander("See Calculation"):
        st.write(f"Area of {shape} is {area}")
        st.write(f"Perimeter of {shape} is {perimeter}")