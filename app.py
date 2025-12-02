import streamlit as st
import pages.processing as processing
import pages.matrix_demo as matrix_demo
import pages.team as team

st.set_page_config(page_title="Image Tools — Final Project", layout="wide")

st.title("Image Tools — Final Project")
st.sidebar.title("Navigation Menu")

page = st.sidebar.selectbox(
    "Pilih Halaman",
    ["Home", "Image Processing Tools", "Matrix Demo", "Team Members"]
)

if page == "Home":
    st.header("Selamat Datang!")
    st.write("""
    Ini adalah aplikasi final project yang berisi:
    - Image Processing Tools (Transform, Filter, BG Removal)
    - Matrix Transformation Demo
    - Team Members
    """)
    st.info("Gunakan sidebar untuk pindah halaman.")
elif page == "Image Processing Tools":
    processing.run()
elif page == "Matrix Demo":
    matrix_demo.run()
elif page == "Team Members":
    team.run()
