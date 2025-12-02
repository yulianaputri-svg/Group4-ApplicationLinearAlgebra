import streamlit as st

def run():
    st.title("👥 Team Members")

    members = [
        ("Zahara Amalia", "Make a Report and Design", "assets/zahara.png"),
        ("Yuliana Bella", "Developer & Programmer", "assets/bella.png"),
        ("Kayla Zavanna", "Make a Report and Research Literature Review", "assets/kayla.png"),
        ("Andhika Ramadhan", "Testing & Developer", "assets/andhika.png")
    ]

    for name, role, photo in members:
        st.subheader(name)
        st.write(f"**Role:** {role}")
        st.image(photo, width=180)
        st.markdown("---")
