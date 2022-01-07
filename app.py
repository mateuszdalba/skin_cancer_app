import streamlit as st
import pickle
import numpy as np


from pages.camera_page import show_camera_page
from pages.image_page import show_image_page
from pages.general_page import show_general_page


st.set_page_config(page_title='Skin cancer - educational app', page_icon="♋")

st.sidebar.title("Navigation bar")
page = st.sidebar.radio('Go To:',
                 ['Main page',
                  'Predict with image',
                  'Live prediction'
                  ])


st.sidebar.title("Responsibility")
st.sidebar.error(
    """
    The algorithm is still in prototype version.
    Author does not take any responsibility for predictions.
    This app is only for educational purposes.
    """
    )


st.sidebar.title("Technical info")
st.sidebar.info(
    """
    Architecture: InceptionV3  \n
    Dataset: HAM10000  \n
    Model accuracy: ~69% \n
    App latest update: 07.01.2022  \n
    """
    )

st.sidebar.title("About")
st.sidebar.info(
    """
    This app is maintained by Mateusz Dalba.  \n
    Linkedin:
    https://www.linkedin.com/in/mateusz-dalba-82184a115/.
    """
    )


if page == 'Live prediction':
    show_camera_page()
elif page =='Predict with image':
    show_image_page()
elif page =='Main page':
    show_general_page()


