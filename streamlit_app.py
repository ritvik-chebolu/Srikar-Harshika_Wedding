import streamlit as st
from PIL import Image

from streamlit_option_menu import option_menu

st.balloons()

selected = option_menu(
    menu_title = None,
    options = ["Invitation", "Bride", "Groom"],
    orientation = "horizontal"
)

if selected == "Invitation":
    st.markdown("<h1 style='text-align: center; color: pink;'>Srikar &hearts; Weds &hearts; Harshika</h1>",
                unsafe_allow_html=True)

    col1, col2 = st.columns(2, gap='small')

    with col1:
        col1.header("*Wedding Invitation*")
        st.write(
            "The Chebolu's and Puvvada's families are excited to invite you to embrace our elated wedding ceremony "
            "with us:")
        st.markdown("<h2 style='text-align: center; color: white;'>Dr. Srikar</h2>", unsafe_allow_html=True)
        st.caption("(M.D. General Medicine, D.N.B. General Medicine)")
        st.markdown("<h4 style='text-align: center; color: white;'>Weds</h4>", unsafe_allow_html=True)
        st.markdown("<h2 style='text-align: center; color: white;'>Dr. Harshika</h2>", unsafe_allow_html=True)
        st.caption("(M.D. General Medicine)")
        st.write("You are cordially invited to attend this auspicious occasion.")
        st.markdown("<h5 style='text-align: center; color: white;'>Date: 12th August, 2022</h5>",
                    unsafe_allow_html=True)
        st.markdown("<h5 style='text-align: center; color: white;'>Time: 8:01 PM (summuhurtham)</h5>",
                    unsafe_allow_html=True)
        st.write("Dinner: 7:00 PM onwards, at the venue")
        st.markdown("<h5 style='text-align: center; color: white;'>Place: Hotel Fortune Inn Sree Kanya</h5>",
                    unsafe_allow_html=True)
        st.write("(Diamond Park Rd., near Sono Vision, Dwarakanagar, Visakhapatnam)")

    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.markdown("<h5 style='text-align: center; color: white;'>Afraid you cannot attend in-person?</h5>",
                unsafe_allow_html=True)
    st.write("Nothing to worry about, this pandemic got you covered.")
    st.write("We will be streaming the event live and will be ***sharing the link on this website soon***. "
             "Please check back sometime closer to the 12th of August for the livestream link.")

    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write(
        "***Please navigate using the links on the top of this page to learn more about the bride and the groom.***")

    with col2:
        st.write("    ")
        st.write("    ")
        st.write("    ")
        st.write("    ")
        st.write("    ")
        st.write("    ")
        couple = Image.open("couple.jpeg")
        col2.image(couple, use_column_width=True)


if selected == "Bride":
    st.markdown("<h1 style='text-align: center; color: pink;'>Srikar &hearts; Harshika</h1>",
                    unsafe_allow_html=True)
    st.snow()

    st.write("We are pleased to invite you to the wedding of Srikar with Harshika.")
    st.write("Here's a little background about Dr. Harshika:")

    col1, col2 = st.columns(2)

    with col1:
        hasi = Image.open('Harshika.jpg')
        col1.header("The Bride")
        col1.image(hasi, use_column_width=True)

    with col2:
            # col2.header("Introduction:"
        st.write("    ")
        st.write("    ")
        st.write("    ")
        st.write("    ")
        col2.caption("Learn more about the Bride:")
            # st.write("    ")
        st.write(
            "Dr. Harshika is currently a Post Graduate in Gandhi Medical Hospital, Hyderabad and is pursuing her"
            "M.D. General Medicine. She previously completed her MBBS degree from Andhra Medical College "
            "(AMC) in Visakhapatnam.")
        st.write("She has been an outstanding athlete during her childhood with several medals, certificates and "
                "championship trophies in Roller Skating, throughout her schooling.")
        st.write(
            "Harshika also enjoys K-Drama and music in her free time (one that is a rarity among doctors these days), "
            "while also being a fan of movies and interesting TV series.")


if selected == "Groom":
    st.markdown("<h1 style='text-align: center; color: pink;'>Srikar &hearts; Harshika</h1>",
                unsafe_allow_html=True)
    st.snow()

    st.write("We are pleased to invite you to the wedding of Srikar with Harshika.")
    st.write("Here's a little background about Dr. Srikar:")

    col1, col2 = st.columns(2)

    with col1:
        col1.header("The Groom")
        col1.caption("About the Groom:")
            # st.write("    ")
        st.write(
            "Dr. Srikar has been in Mumbai for the past few years. He completed his M.D. General Medicine followed"
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