import streamlit as st
from PIL import Image

# 画像表示
st.write('Display Image')
img1 = Image.open('octocat1.png')
img2 = Image.open('octocat2.jpeg')
st.image(img1, caption='octocat1', use_column_width=True)

# ボタンで画像表示、非表示
if st.checkbox('show octocat2?'):
    st.image(img2, caption='octocat2', use_column_width=True)
