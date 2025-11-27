import streamlit as st
from PIL import Image
import numpy as np
import tensorflow as tf
from pdf_generator import generate_pdf
import io

st.set_page_config(page_title="Tomato Plant Disease Classifier",layout="centered")
st.title("Tomato Plant Disease Classifier")

@st.cache_resource
def load_model():
    tf.keras.models.load_model("version_1.keras")

model = load_model()

CLASS_NAMES = ['Tomato_Bacterial_spot',
 'Tomato_Early_blight',
 'Tomato_Late_blight',
 'Tomato_Leaf_Mold',
 'Tomato_Septoria_leaf_spot',
 'Tomato_Spider_mites',
 'Tomato_Tomato_YellowLeaf_Curl_Virus',
 'Tomato_Tomato_mosaic_virus',
 'Tomato__Target_Spot',
 'Tomato_healthy']

option = st.radio("Choose Input Method:",["Upload Image","Take a Photo"])

uploaded_image = None
if option == "Upload Image":
    uploaded_image = st.file_uploader("Upload a tomato leaf image",type=["jpg", "jpeg", "png"])
elif option == "Take a Photo":
        uploaded_image = st.camera_input("Take a picture")

if uploaded_image:
    st.subheader("Selected Image")
    img = Image.open(uploaded_image)
    st.image(img, width=300)
    if st.button("Predict Disease"):
        st.info("Predicting....")

        image_array = img.convert("RGB").resize((96,96))
        image_array = np.array(image_array)/225.0
        image_array = np.expand_dims(image_array,axis=0)

        preds = model.predict(image_array)[0]
        disease = CLASS_NAMES[np.argmax(preds)]
        confidence = round(float(preds[np.argmax(preds)])*100, 2)

        st.success(f"Prediction: {disease}")
        st.write(f"Confidence: {confidence}")

        pdf_path = generate_pdf(uploaded_image,disease,confidence)
        with open(pdf_path,"rb") as pdf_file:
             st.download_button(
                "Download PDF Report",
                data=pdf_file,
                file_name="tomato_diagnosis_report.pdf",
                mime="application/pdf"
            )