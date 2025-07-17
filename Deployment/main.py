
from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
import joblib
from PIL import Image
import numpy as np
import io
import tensorflow as tf
from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
import joblib
from PIL import Image
import numpy as np
import io
import tensorflow as tf
app = FastAPI()
# Allow Streamlit to access the API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # You can restrict this in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# Load model
from tensorflow.keras.models import load_model
import h5py

model = tf.keras.models.load_model("model_directory")
classes = [
    "Acne", "Actinic Carcinoma", "Atopic Dermatitis", "Bullous Disease", "Cellulitis",
    "Eczema", "Drug Eruptions", "Herpes HPV", "Light Diseases", "Lupus", "Melanoma",
    "Poison IVY", "Psoriasis", "Benign Tumors", "Systemic Disease", "Ringworm",
    "Urticarial Hives", "Vascular Tumors", "Vasculitis", "Viral Infections"
]
def preprocess_image(image_bytes):
    image = Image.open(io.BytesIO(image_bytes)).convert("RGB")
    image = image.resize((224, 224))
    image_array = np.array(image) / 255.0
    image_array = np.expand_dims(image_array, axis=0)  # shape: (1, 224, 224, 3)
    return image_array
@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    image_bytes = await file.read()
    img = preprocess_image(image_bytes)
    prediction = model.predict(img)
    class_index = np.argmax(prediction)
    class_name = classes[class_index]
    confidence = float(np.max(prediction))

    return {"prediction": class_name, "confidence": round(confidence, 3)}