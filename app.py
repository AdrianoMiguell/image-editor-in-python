import streamlit as st
from PIL import Image
from PIL.ImageFilter import *

st.markdown("<h1 style='text-align: center;'> Image Editor </h1>", unsafe_allow_html=True)
st.markdown("---")
image = st.file_uploader("Upload Your Image", type=['jpg', 'png', 'jpeg'])

info = st.empty()
size = st.empty()
mode = st.empty()
format_ = st.empty()
message_ = st.empty()

if image: 
    img = Image.open(image)
    info.markdown("<h2 style='text-align: center;'> Information </h2>", unsafe_allow_html=True)
    size.markdown(f"<h6> Size: {img.size} </h6>", unsafe_allow_html=True)
    mode.markdown(f"<h6> Mode: {img.mode} </h6>", unsafe_allow_html=True)
    format_.markdown(f"<h6> Format: {img.format} </h6>", unsafe_allow_html=True)
    
    st.markdown("<h2 style='text-align: center;'> Resizing </h2>", unsafe_allow_html=True)
    resCol1, resCol2 = st.columns(2)
    width=resCol1.number_input("Width", value=img.width)
    height = resCol2.number_input("Height", value=img.height)
    
    st.markdown("<h2 style='text-align: center;'> Rotation </h2>", unsafe_allow_html=True)
    degree = st.number_input("Degree")
    
    st.markdown("<h2 style='text-align: center;'> Filter </h2>", unsafe_allow_html=True)
    filters = st.selectbox("Filters", options=("None", "Blur", "Contour", "Detail", "Emboss","Sharpen", "Smooth"))
    
    s_btn = st.button("Submit")
    
    if s_btn:
        edited = img.resize((width, height)).rotate(degree)
        filtered = edited
        
        if filters != "None":
            if filters == "Blur": 
                filtered = edited.filter(BLUR)
            elif filters == "Contour":
                filtered = edited.filter(CONTOUR)
            elif filters == "Detail":
                filtered = edited.filter(DETAIL)
            elif filters == "Emboss":
                filtered = edited.filter(EMBOSS)
            elif filters == "Sharpen":
                filtered = edited.filter(SHARPEN)
            elif filters == "Smooth":
                filtered = edited.filter(SMOOTH)
            else:
                message_.warning("Error in choose the filter")
    
        st.image(filtered)
    