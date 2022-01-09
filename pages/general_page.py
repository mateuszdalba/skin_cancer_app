import streamlit as st
import random
import os
#from os import listdir
from PIL import Image 
import pandas as pd

def show_general_page():
    st.title('Examine changes on your skin')

    #path2 = os.path.realpath("./model/model_skin.h5")
    #st.write(path2)

    st.error('Warning ! Some photos might be drastic. ')

    st.markdown("""  
    Skin cancer is a major public health problem, with over 5,000,000 newly diagnosed cases in the United States every year.  
    Melanoma is the deadliest form of skin cancer, responsible for an overwhelming majority of skin cancer deaths. 
    In 2015, the global incidence of melanoma was estimated to be over 350,000 cases, with almost 60,000 deaths.  
    Although the mortality is significant, when detected early, melanoma survival exceeds 95%.  
    Source: https://challenge.isic-archive.com/ 
    """)


    roll = st.button('Generate example picture')

    if roll == True:

        df = pd.read_csv("df.csv")
        pic = random.choice(os.listdir('data'))
        id = pic.split('.')[0]
        tmp = df.loc[df['image_id'] == id]
        #st.dataframe(tmp)
        full_path =  f"data/{pic}"
        im = Image.open(full_path)
        st.image(im)
        age = tmp['age']
        image_id = tmp['image_id']
        target = tmp['dx']
        sex = tmp['sex']
        localization = tmp['localization']

        st.markdown(f"""
        
        Image ID: {image_id.iloc[0]}  \n
        Patient's age: {age.iloc[0]}  \n
        Sex: {sex.iloc[0]}  \n
        Localization: {localization.iloc[0]}  \n
        Label: {target.iloc[0]}  \n
        
        """)

    
    labels = st.button('Show labels description')

    if labels == True:

        st.markdown("""
        AKIEC: Actinic keratoses and intraepithelial carcinoma / Bowens disease  \n  
        BCC: basal cell carcinoma  \n
        BKL: benign keratosis-like lesions (solar lentigines / seborrheic keratoses and lichen-planus like keratoses)  \n
        DF: dermatofibroma  \n
        MEL: melanoma  \n
        NV: melanocytic nevi  \n
        VASC: vascular lesions (angiomas, angiokeratomas, pyogenic granulomas and hemorrhage)  \n
        """)
        
