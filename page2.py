import streamlit as st
from PIL import Image

st.markdown("<h1 style='text-align: center; color: pink;'>Srikar &hearts; Harshika</h1>", unsafe_allow_html=True)
st.snow()

st.write("We are pleased to invite you to the wedding of Srikar with Harshika.")
st.write("Here's a little background about Dr. Srikar:")

col1, col2 = st.columns(2)

with col1:
    col1.header("The Groom")
    col1.caption("About the Groom:")
    # st.write("    ")
    st.write("Dr. Srikar has been in Mumbai for the past few years. He completed his M.D. General Medicine followed"
             "by D.N.B. General Medicine in J.J. Hospital, Mumbai.")
    st.write("Srikar is a ______________________________________________________________________________"
             "_______________________________________________________________________________________")
    st.write("Srikar also enjoys ______________________________________________________________________"
             "_____________________________________________________________________________.")

with col2:
    # col2.header("Introduction:"
    st.write("    ")
    st.write("    ")
    st.write("    ")
    st.write("    ")
    srikar = Image.open('Srikar.jpeg')
    col2.image(srikar, use_column_width=True)

