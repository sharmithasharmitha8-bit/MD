import streamlit as st
import numpy as np

# --------------------------------------------------
# Page config (must be first Streamlit call)
# --------------------------------------------------
st.set_page_config(
    page_title="Prediction App",
    page_icon="🤖",
    layout="centered"
)

# --------------------------------------------------
# Simple model logic (no sklearn)
# --------------------------------------------------
def predict_manipulator(features):
    """
    Simple weighted logic model
    Replace weights if needed
    """
    weights = np.array([0.5, 0.3, 0.6, 0.4, 0.7, 0.5])
    score = np.dot(features, weights)

    return 1 if score > 5 else 0


# --------------------------------------------------
# UI
# --------------------------------------------------
st.title("Best Model Prediction System")

st.subheader("Enter Input Values")

col1, col2 = st.columns(2)

with col1:
    f1 = st.number_input("Feature 1", step=0.1)
    f2 = st.number_input("Feature 2", step=0.1)
    f3 = st.number_input("Feature 3", step=0.1)

with col2:
    f4 = st.number_input("Feature 4", step=0.1)
    f5 = st.number_input("Feature 5", step=0.1)
    f6 = st.number_input("Feature 6", step=0.1)

# --------------------------------------------------
# Prediction
# --------------------------------------------------
if st.button("🔍 Predict", use_container_width=True):
    input_data = np.array([f1, f2, f3, f4, f5, f6])
    prediction = predict_manipulator(input_data)

    st.markdown("---")

    if prediction == 1:
        st.success("✅ RESULT: MANIPULATOR")
    else:
        st.error("❌ RESULT: NOT A MANIPULATOR")
