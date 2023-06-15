"""
# My first app
"""

import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import sadpanda_api as spd_api
import json
import requests

st.title('Access Sadpanda API')


url = st.text_input('Sadpanda gallery url:', 'e.g: https://e-hentai.org/g/2574478/7521f9f1db/')

if not url:
    st.write("Please insert a correct url.")

urls = [url]
# st.write(urls)
#Send post request to API
resp = spd_api.send_api(urls)


st.write("The gallery's title is: ", resp[0]['title'])
#view json response
# st.write(resp)

st.download_button('Download gdata as a text file', json.dumps(resp[0]))

# img_url = 'https://ehgt.org/6e/94/6e94115f80e4dfa60ac1033a6d76bb6c22c4e0f2-1627347-1433-2024-jpg_l.jpg'

img_url = resp[0]['thumb']
image = Image.open(requests.get(img_url, stream=True).raw)
st.image(image, caption=resp[0]['title'])


# df = pd.read_csv('most-recent.csv')
# df.img = 'cover_images\\' + df.img
# df = df.iloc[:50] # store only the first 50 rows


# # Display images in rows
# for index, row in df.iterrows():
#     col1, col2 = st.columns(2)
#     with col1:
#         st.write(row['title'], unsafe_allow_html=True)
#     with col2:
#         try:
#             st.image(row['img'], width=200)
#             st.write(row['title'], unsafe_allow_html=True)
#             st.write('https://www.dmm.co.jp/dc/doujin/', unsafe_allow_html=True)
#         except:
#             st.write('.')

