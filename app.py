from flask import Flask, render_template, request
import joblib
import numpy as np
import cv2
from PIL import Image
import os

app = Flask(__name__)

model = joblib.load("models/malaria_model.pkl")

IMG_SIZE = 64
CLASS_NAMES = ["Parasitized", "Uninfected"]

def prepare_image(image):
    """Convert PIL image to grayscale, resize, normalize, and flatten with enhancement"""
    image = image.convert("L")  # Convert to grayscale
    image = image.resize((IMG_SIZE, IMG_SIZE))
    image_array = np.array(image)
    
    # Histogram equalization to improve contrast
    image_array = cv2.equalizeHist(image_array)
    
    # Normalize to 0-1
    image_array = image_array / 255.0
    image_flat = image_array.flatten()  # Flatten to 1D
    return image_flat

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def predict():
    file = request.files['file']
    image = Image.open(file)
    
    try:
        processed = prepare_image(image)
        processed = processed.reshape(1, -1)  # Reshape for prediction
        
        prediction = model.predict(processed)[0]
        proba = model.predict_proba(processed)[0]
        confidence = max(proba) * 100
        
        label = CLASS_NAMES[int(prediction)]
        
        # Debug output
        print(f"Prediction: {prediction}, Probabilities: {proba}, Label: {label}")
        
        return render_template("index.html",
                               prediction=label,
                               confidence=round(float(confidence), 2))
    except Exception as e:
        print(f"Error: {str(e)}")
        return render_template("index.html",
                               prediction="Error",
                               confidence=f"Failed to process image: {str(e)}")

if __name__ == '__main__':
    app.run(debug=True)
