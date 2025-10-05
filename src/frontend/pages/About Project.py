import streamlit as st
from PIL import Image

image = Image.open("pictures/logo.png")
st.image(image, use_container_width=True)

st.title("About Project")

st.markdown("""

# In this project we'd like to present you a tool for **AI-driven exoplanet discovery**.
 
""")

st.markdown("---")
st.page_link("Home.py", label="⬅️ Back to Main Page", icon="🏠")