import os
import numpy as np
import cv2
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

DATA_DIR = "dataset"
IMG_SIZE = 64  # Smaller size for faster processing

data = []
labels = []

print("Checking dataset directories...")
for category in ["parasitized", "uninfected"]:
    path = os.path.join(DATA_DIR, category)
    if not os.path.isdir(path):
        raise FileNotFoundError(f"Folder '{path}' not found. Make sure you have placed your images correctly.")

print("Loading images and preprocessing...")
for category in ["parasitized", "uninfected"]:
    path = os.path.join(DATA_DIR, category)
    class_num = 0 if category == "parasitized" else 1

    for img in os.listdir(path):
        img_path = os.path.join(path, img)
        image = cv2.imread(img_path)
        if image is None:
            print(f"Warning: failed to read {img_path}")
            continue
        image = cv2.resize(image, (IMG_SIZE, IMG_SIZE))
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # Convert to grayscale
        image = cv2.equalizeHist(image)  # Histogram equalization for better contrast
        image = image / 255.0
        image_flat = image.flatten()  # Flatten to 1D array
        data.append(image_flat)
        labels.append(class_num)

print(f"Total images loaded: {len(data)}")

X = np.array(data)
y = np.array(labels)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print("Training Random Forest model...")
model = RandomForestClassifier(n_estimators=100, random_state=42, n_jobs=-1, verbose=1)
model.fit(X_train, y_train)

print("Evaluating model...")
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Test Accuracy: {accuracy:.4f}")
print("\nClassification Report:")
print(classification_report(y_test, y_pred, target_names=["Parasitized", "Uninfected"]))

print("\nSaving model...")
joblib.dump(model, "models/malaria_model.pkl")
print("Model Training Complete")
