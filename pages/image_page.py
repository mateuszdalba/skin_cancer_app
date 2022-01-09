import streamlit as st
#import cv2
from PIL import Image 
#import PIL 
import numpy as np
from functions.load_and_predict import predict




def show_image_page():

    st.title('Predict skin cancer using uploaded photo')

    st.info('In order to properly examine skin ensure that the photo shows only skin lesion.')

    image_file = st.file_uploader("Upload Images", type=["png","jpg","jpeg"])

    if image_file is not None:
        

        file_details = {"filename":image_file.name, "filetype":image_file.type, "filesize":image_file.size}
        #st.write("File details:   \n",file_details)
        st.image(image_file)
        im = Image.open(image_file)
        im = np.array(im)
        
        names, all_probabilities, max_prob = predict(image=im)

        st.write('Model prediction: ', names[0])
        st.write('Probability: ', max_prob)
        st.write('All probabilites: ',all_probabilities)
       

        labels = st.button('Show labels descriptions')
        if labels == True:
            st.markdown("""
            Possible results from algorithm:  \n
            AKIEC (0): Actinic keratoses and intraepithelial carcinoma / Bowens disease  \n  
            BCC (1): basal cell carcinoma  \n
            BKL (2): benign keratosis-like lesions (solar lentigines / seborrheic keratoses and lichen-planus like keratoses)  \n
            DF (3): dermatofibroma  \n
            MEL (4): melanoma  \n
            NV (5): melanocytic nevi  \n
            VASC (6): vascular lesions (angiomas, angiokeratomas, pyogenic granulomas and hemorrhage)  \n
            """)
        
    
       