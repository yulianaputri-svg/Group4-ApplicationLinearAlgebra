import streamlit as st
from PIL import Image
import numpy as np
import io
from utils import (
    pil_to_numpy, numpy_to_pil,
    translation_matrix, scaling_matrix, rotation_matrix,
    shear_matrix, reflection_matrix, apply_affine_transform
)

def run():
    st.title("Image Processing Tools")

    uploaded = st.file_uploader("Upload gambar", type=["png","jpg","jpeg"])
    if not uploaded:
        st.info("Upload dulu gambarnya 😊")
        return

    img = Image.open(uploaded).convert("RGBA")
    arr = pil_to_numpy(img)
    h, w = img.size[1], img.size[0]
    cx, cy = w/2, h/2

    st.image(img, width=300)

    mode = st.sidebar.selectbox("Pilih Mode", ["Transformations", "Filters"])

    if mode == "Transformations":
        tf = st.sidebar.selectbox("Jenis Transformasi", 
            ["Translation", "Scaling", "Rotation", "Shearing", "Reflection"]
        )

        if tf == "Translation":
            tx = st.sidebar.slider("Tx", -w, w, 0)
            ty = st.sidebar.slider("Ty", -h, h, 0)
            M = translation_matrix(tx, ty)

        elif tf == "Scaling":
            sx = st.sidebar.slider("Scale X", 0.1, 3.0, 1.0)
            sy = st.sidebar.slider("Scale Y", 0.1, 3.0, 1.0)
            M = scaling_matrix(sx, sy, (cx, cy))

        elif tf == "Rotation":
            ang = st.sidebar.slider("Angle", -180, 180, 0)
            M = rotation_matrix(ang, (cx, cy))

        elif tf == "Shearing":
            shx = st.sidebar.slider("Shear X", -1.0, 1.0, 0.0)
            shy = st.sidebar.slider("Shear Y", -1.0, 1.0, 0.0)
            M = shear_matrix(shx, shy)

        elif tf == "Reflection":
            axis = st.sidebar.selectbox("Axis", ["x", "y"])
            M = reflection_matrix(axis)

        out = apply_affine_transform(arr, M)
        out_pil = numpy_to_pil(out)

        st.image(out_pil, width=350)

    else:
        st.write("Filter sederhana belum ditambahkan di versi ini 😁 (opsional)")
