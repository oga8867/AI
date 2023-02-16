# import numpy as np
# import pandas as pd
# import io
# import os
# from  PIL import Image
# import cv2
# from streamlit_webrtc import VideoTransformerBase, webrtc_streamer

# def app():
#     st.title("Webcam Test")
#     webrtc_ctx = webrtc_streamer(key="example")#, video_transformer_factory=VideoTransformer)

# app()

import streamlit as st

picture = st.camera_input("Take a picture")

if picture:
    st.image(picture)

#실행   streamlit run main.py
