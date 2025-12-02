import streamlit as st
import numpy as np
from utils import translation_matrix, scaling_matrix, rotation_matrix

def run():
    st.title("Matrix Demo")

    x = st.number_input("x", value=10.0)
    y = st.number_input("y", value=20.0)

    st.subheader("Translation")
    tx = st.slider("Tx", -50, 50, 10)
    ty = st.slider("Ty", -50, 50, 5)
    Mt = translation_matrix(tx, ty)
    st.write(Mt)
    res_t = Mt @ np.array([x, y, 1])
    st.write("Hasil:", res_t[:2])

    st.subheader("Rotation")
    ang = st.slider("Angle", -180, 180, 0)
    Mr = rotation_matrix(ang)
    st.write(Mr)
    res_r = Mr @ np.array([x, y, 1])
    st.write("Hasil:", res_r[:2])
