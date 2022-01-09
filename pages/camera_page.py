import streamlit as st
import cv2

from functions.load_and_predict import predict

def show_camera_page():
    st.title('Predict cancer using webcam')
    
    st.info('Turn on webcam and zoom in on skin lesion and click "predict".')
    run = st.checkbox('Turn on webcam')
    FRAME_WINDOW = st.image([])
    
    camera = cv2.VideoCapture(0, cv2.CAP_DSHOW) 
    make_prediction = st.checkbox('Execute prediction')

    while run:
        _, frame = camera.read()
        
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        FRAME_WINDOW.image(frame)
        if make_prediction == True:
            names, all_probabilities, max_prob = predict(image=frame)
            #st.write(names, all_probabilities, max_prob)

            st.write('Model prediction: ', names[0])
            st.write('Probability: ', max_prob)
            st.write('All probabilites: ',all_probabilities)

            break

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

