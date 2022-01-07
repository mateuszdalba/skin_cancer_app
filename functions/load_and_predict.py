from tensorflow import keras
import tensorflow as tf
import os 
import matplotlib.pyplot as plt
import numpy as np
import cv2
import pandas as pd
from keras.preprocessing.image import load_img
import glob 
import shutil


def predict(image):

    model = tf.keras.models.load_model('model_skin.h5')
    
    gender_target = {0:'Bowens disease',1:'basal cell carcinoma',2:'benign keratosis-like lesions',3:'dermatofibroma',4:'melanoma',5:'melanocytic nevi',6:'vascular lesions'}

    im = cv2.resize(cv2.cvtColor(image, cv2.COLOR_BGR2RGB), (178, 218)).astype(np.float32) / 255.0
    im = np.expand_dims(im, axis = 0)

    model.compile(loss = 'categorical_crossentropy',
                  metrics=['accuracy'])
    
    prediction = model.predict(im)
    all_probabilities = prediction

    classes = np.argmax(prediction, axis=-1)
    names = [gender_target[i] for i in classes]

    max_prob = np.max(all_probabilities)

    return names, all_probabilities, max_prob
