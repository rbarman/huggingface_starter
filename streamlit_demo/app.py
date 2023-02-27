import streamlit as st
from io import StringIO
import requests
import base64

API_URL = 'https://hf.space/embed/rbarman/resnet50-example/+/api/predict'

uploaded_file = st.file_uploader("Choose a file", type=['jpg'])
if uploaded_file is not None:
    
    # create base64 url of uploaded image
    bytes_data = uploaded_file.getvalue()
    prefix = f'data:image/jpg;base64,'
    url = prefix + base64.b64encode(bytes_data).decode('utf-8')

    # call api
    resp = requests.post(
            API_URL, 
            json={'data':[url]}
        )
    print(resp.json())

    # display classification label
    label = resp.json()['data'][0]['label']
    st.text(label)