
import streamlit as st
import requests
from PIL import Image
import streamlit as st
import requests
from PIL import Image
st.set_page_config(page_title="Skin Disease Detector", layout="centered")

st.title("Skin Disease Detection App")
st.markdown("Upload a skin lesion image to detect the possible skin disease.")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="Uploaded Image", use_column_width=True)

    if st.button("Predict"):
        with st.spinner("Analyzing..."):
            try:
                # Properly format the file for FastAPI
                files = {"file": (uploaded_file.name, uploaded_file.getvalue(), "image/png")}
                response = requests.post("http://localhost:8000/predict", files=files)

                if response.status_code == 200:
                    result = response.json()
                    st.success(f"Predicted Skin Disease: **{result['prediction']}**")
                    st.info(f"Confidence: {result['confidence']*100:.2f}%")
                else:
                    st.error("Prediction failed. Check the API server.")
            except Exception as e:
                st.error("An error occurred.")
                st.exception(e)