import streamlit as st
import numpy as np
import joblib

# --------------------------------------------------
# Load trained best model
# --------------------------------------------------
model = joblib.load("best_model.pkl")

# --------------------------------------------------
# Page config
# --------------------------------------------------
st.set_page_config(
    page_title="Prediction App",
    page_icon="🤖",
    layout="centered"
)

# --------------------------------------------------
# Title
# --------------------------------------------------
st.markdown(
    "<h2 style='text-align: center;'>Best Model Prediction System</h2>",
    unsafe_allow_html=True
)

st.markdown("---")

# --------------------------------------------------
# Input Section (MATCH THIS WITH YOUR HTML FIELDS)
# --------------------------------------------------
st.subheader("Enter Input Values")

col1, col2 = st.columns(2)

with col1:
    f1 = st.number_input("Feature 1", min_value=0.0, step=0.1)
    f2 = st.number_input("Feature 2", min_value=0.0, step=0.1)
    f3 = st.number_input("Feature 3", min_value=0.0, step=0.1)

with col2:
    f4 = st.number_input("Feature 4", min_value=0.0, step=0.1)
    f5 = st.number_input("Feature 5", min_value=0.0, step=0.1)
    f6 = st.number_input("Feature 6", min_value=0.0, step=0.1)

# --------------------------------------------------
# Predict Button
# --------------------------------------------------
st.markdown("")

if st.button("🔍 Predict", use_container_width=True):

    input_data = np.array([[f1, f2, f3, f4, f5, f6]])

    prediction = model.predict(input_data)[0]

    st.markdown("---")

    # --------------------------------------------------
    # Output
    # --------------------------------------------------
    if prediction == 1:
        st.success("✅ RESULT: MANIPULATOR")
    else:
        st.error("❌ RESULT: NOT A MANIPULATOR")
