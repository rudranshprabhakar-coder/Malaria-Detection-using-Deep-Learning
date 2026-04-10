# Advanced Malaria Detection System
#
# Using Deep Learning to Detect Malaria Parasites

## Project Overview

Malaria is a life-threatening disease caused by parasites transmitted through mosquito bites. Early and accurate detection is crucial for effective treatment.

This project implements a **Deep Learning–based malaria detection system** that classifies microscopic blood smear images as **Parasitized** or **Uninfected** using a **Convolutional Neural Network (CNN)**.

The system also includes a **web interface built using Flask**, allowing users to upload an image and receive a prediction instantly.

---

# Features

* Deep Learning model for malaria cell classification
* Custom **Convolutional Neural Network (CNN)**
* Image classification into:

  * **Parasitized**
  * **Uninfected**
* Web interface using **Flask**
* Trained model saved as `.pkl`
* Image upload and prediction system

---

# Project Structure

```
Malaria-Detection-using-Deep-Learning
│
├── dataset
│   ├── parasitized
│   └── uninfected
│
├── models
│   └── malaria_model.pkl
│
├── static
│   └── css
│       └── style.css
│
├── templates
│   └── index.html
│
├── app.py
├── train_model.py
├── requirements.txt
├── .gitignore
```

### Explanation

| File/Folder    | Description                            |
| -------------- | -------------------------------------- |
| dataset        | Contains training images               |
| parasitized    | Images of malaria infected cells       |
| uninfected     | Images of healthy cells                |
| models         | Stores the trained deep learning model |
| app.py         | Flask web application                  |
| train_model.py | Script used to train the CNN model     |
| templates      | HTML files for the web interface       |
| static/css     | Styling for the web application        |

---

# Dataset

The dataset used in this project consists of **microscopic images of blood cells** categorized into:

* **Parasitized**
* **Uninfected**

The images are used to train the CNN model to detect malaria parasites.

Dataset Structure:

```
dataset/
    parasitized/
    uninfected/
```

---

# Model Architecture

The model is based on a **Convolutional Neural Network (CNN)** which includes:

* Convolution Layers
* ReLU Activation
* Max Pooling Layers
* Fully Connected Layers
* Sigmoid Output Layer for binary classification

The CNN automatically learns important features from microscopic cell images.

---

# Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/Malaria-Detection-using-Deep-Learning.git
```

### 2. Navigate to the Project Folder

```bash
cd Malaria-Detection-using-Deep-Learning
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Training the Model

To train the CNN model, run:

```bash
python train_model.py
```

The trained model will be saved in the **models folder**.

---

# Running the Web Application

Start the Flask application:

```bash
python app.py
```

Then open your browser and go to:

```
http://127.0.0.1:5000
```

Upload a blood cell image and the system will predict whether it is **Parasitized** or **Uninfected**.

---

# Technologies Used

* Python
* TensorFlow / Keras
* NumPy
* OpenCV
* Flask
* HTML / CSS
* Deep Learning (CNN)

---

# Results

The trained CNN model achieves **high accuracy in detecting malaria parasites from microscopic images**, demonstrating the effectiveness of deep learning in medical image analysis.

---

# Future Improvements

* Improve model accuracy with deeper architectures
* Deploy the application using **Docker or Cloud**
* Add **real-time microscope image integration**
* Improve UI/UX of the web application
* Implement **multi-class malaria parasite detection**

---
GitHub:
[https://github.com/rudranshprabhakar-coder](https://github.com/rudranshprabhakar-coder)

---
