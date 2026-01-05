import streamlit as st
import numpy as np
from sklearn.svm import SVC
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split

# --------------------------------------------------
# Page config (MUST be first Streamlit command)
# --------------------------------------------------
st.set_page_config(
    page_title="Prediction App",
    page_icon="🤖",
    layout="centered"
)

# --------------------------------------------------
# Train model inside app.py (ONE FILE ONLY)
# --------------------------------------------------
@st.cache_resource
def train_model():
    # 🔹 Example dummy dataset
    # Replace this with YOUR dataset logic if needed
    X, y = make_classification(
        n_samples=500,
        n_features=6,
        n_informative=4,
        n_classes=2,
        random_state=42
    )

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = SVC(kernel="rbf", probability=True)
    model.fit(X_train, y_train)

    return model

model = train_model()

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

    input_data = np.array([[f1, f2, f3, f4, f5, f6]])
    prediction = model.predict(input_data)[0]

    st.markdown("---")

    if prediction == 1:
        st.success("✅ RESULT: MANIPULATOR")
    else:
        st.error("❌ RESULT: NOT A MANIPULATOR")
