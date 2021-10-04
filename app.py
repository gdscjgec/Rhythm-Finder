"""
Rhythm-Finder app

This file will take the user
data and predict the songs.


"""

# Libraries ------
import base64
import streamlit as st

# libraries ------

#Background Image Section
main_bg = "assets/bg.jpg"
main_bg_ext = "jpg"
st.markdown(
    f"""
    <style>
    .reportview-container {{
        background: url(data:image/{main_bg_ext};base64,{base64.b64encode(open(main_bg, "rb").read()).decode()});
        background-size: cover;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# Headers ------

st.header('Rhythm-Finder App')

st.subheader('GDSC-JGEC')

# Headres ------


# User Inputs ------

# User Inputs ------


# Model Load and prediction ------

# Model Load and prediction ------


# Footer ------

# Footer ------
