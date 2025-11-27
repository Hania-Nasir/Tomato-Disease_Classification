#Tomato-Plant-Disease-Classifier

This project classifies diseases in tomato plants based on leaf images. It uses a deep learning model to detect diseases such as Early Blight, Late Blight, Leaf Mold, and more.
The main goal is to help farmers and gardeners quickly identify plant diseases and take timely action.

##Project Overview

Plant diseases significantly affect crop yield and quality. Early detection is crucial to prevent widespread damage.
This project applies a convolutional neural network (CNN) model to classify tomato leaf images into multiple disease categories or healthy leaves.
It demonstrates how AI and deep learning can assist in agriculture by providing fast, image-based disease diagnosis.

##Tools and Technologies

Programming Language: Python

Libraries: TensorFlow, Keras, NumPy, Pillow, Streamlit, ReportLab

Model: Deep Learning CNN (multi-class classification)

Deployment Framework: Streamlit (frontend)

Other Tools: Git, GitHub, VS Code

##Project Structure
streamlit_tomato_classifier/
│
├── version_1.keras             # Trained deep learning model
├── app.py                      # Streamlit application
├── pdf_generator.py            # PDF report generation utility
├── requirements.txt            # Project dependencies
└── README.md                   # Project documentation

##Machine Learning Workflow
###Data Preprocessing

Collected and cleaned tomato leaf images for multiple disease classes

Resized and normalized images for model input

Split data into training and validation sets

###Model Training

Trained a CNN model using Keras and TensorFlow

Evaluated model accuracy and loss on validation data

Saved the best model as version_1.keras

###Deployment

Developed a Streamlit app for interactive usage

Users can either upload an image or take a photo using a camera

The app displays the uploaded image, predicts the disease, and shows the confidence score

Generates a PDF report including the image, predicted disease, confidence, and date/time

Fully self-contained and deployable on Streamlit Cloud

###Features

Upload or capture tomato leaf images

Display uploaded/captured image

Predict disease with confidence score

Generate downloadable PDF report with all details

###Author

Hania Nasir

Author

Hania Nasir
