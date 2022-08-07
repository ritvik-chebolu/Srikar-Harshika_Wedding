import streamlit as st
from PIL import Image

st.markdown("<h1 style='text-align: center; color: pink;'>Srikar &hearts; Harshika</h1>", unsafe_allow_html=True)
st.balloons()

st.write("We are pleased to invite you to the wedding of Srikar with Harshika.")
st.write("Here's a little background about Dr. Harshika:")

col1, col2 = st.columns(2)

with col1:
    hasi = Image.open('../Harshika.jpg')
    col1.header("The Bride")
    col1.image(hasi, use_column_width = True)

with col2:
    # col2.header("Introduction:"
    st.write("    ")
    st.write("    ")
    st.write("    ")
    st.write("    ")
    col2.caption("Learn more about the Bride:")
    # st.write("    ")
    st.write("Dr. Harshika is currently a Post Graduate in Gandhi Medical Hospital, Hyderabad and is pursuing her"
             "M.D. General Medicine. She previously completed her MBBS degree from Andhra Medical College "
             "(AMC) in Visakhapatnam.")
    st.write("She has been an outstanding athlete during her childhood with several medals, certificates and "
             "championship trophies in Roller Skating, throughout her schooling.")
    st.write("Harshika also enjoys K-Drama and music in her free time (one that is a rarity among doctors these days), "
             "while also being a fan of movies and interesting TV series.")
