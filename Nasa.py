import requests
import os
import shutil
from PIL import Image
import streamlit as st
import datetime as dt

API_KEY = 'your Api'
BASE_URL = 'https://api.nasa.gov/planetary/apod'

@st.cache(suppress_st_warning=True, show_spinner=False)
def get_nasa_image(date):
    params = {'date': date, 'api_key': API_KEY}
    r = requests.get(BASE_URL, params=params)
    data = r.json()
    title = data['title']
    explanation = data['explanation']
    image_url = data['url']
    image_response = requests.get(image_url, stream=True)
    filename = f'{date}.jpg'
    image_path = os.path.join('Data', 'Nasa_Images', filename)
    with open(image_path, 'wb') as out_file:
        shutil.copyfileobj(image_response.raw, out_file)
    del image_response
    return title, explanation, image_path