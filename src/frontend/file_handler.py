import os
import streamlit as st

def save_uploaded_csv(uploaded_file, save_dir="backend_models/input_data"):
    """
    Save user input in dedicated directory.
    """
    if uploaded_file is None:
        st.warning("No file uploaded.")
        return None

    os.makedirs(save_dir, exist_ok=True)

    save_path = os.path.join(save_dir, uploaded_file.name)

    # Save file
    with open(save_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.success(f" File saved as: {save_path}")
    return save_path

def delete_file_if_exists(file_path):
    """Usuwa plik, jeśli istnieje."""
    if file_path and os.path.exists(file_path):
        os.remove(file_path)
        return True
    return False
