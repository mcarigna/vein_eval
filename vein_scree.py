import streamlit as st
import pandas as pd

# Title and introduction
st.title("Venous Clinical Severity Score (VCSS) Calculator")
st.write("The Venous Clinical Severity Score (VCSS) is used to assess the severity of chronic venous disease.")
st.image('venous reflux image.jpg')
# Create input fields for VCSS components
st.header("VCSS Components")

pain = st.slider("Pain (0-3)", min_value=0, max_value=3, value=0)
varicose_veins = st.slider("Varicose Veins (0-3)", min_value=0, max_value=3, value=0)
edema = st.slider("Edema (0-3)", min_value=0, max_value=3, value=0)
skin_changes = st.slider("Skin Changes (0-3)", min_value=0, max_value=3, value=0)
inflammation = st.slider("Inflammation (0-3)", min_value=0, max_value=3, value=0)
ulcer = st.slider("Ulcer (0-3)", min_value=0, max_value=3, value=0)

# Calculate VCSS score
vcss_score = pain + varicose_veins + edema + skin_changes + inflammation + ulcer

# Display the VCSS score
st.header("VCSS Score")
st.write(f"Your VCSS score is: {vcss_score}")