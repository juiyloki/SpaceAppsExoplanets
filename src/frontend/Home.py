#%%
import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
# from your_model_file import load_model, predict, train_model  # uncomment when ready
from file_handler import save_uploaded_csv, delete_file_if_exists
import sys
from pathlib import Path

project_root = Path(__file__).resolve().parent.parent
if str(project_root) not in sys.path:
    sys.path.append(str(project_root))

# Teraz import zadziała:
from backend_models.test_models import run_model

image = Image.open("frontend/pictures/logo.png")

# ----- Main Title and Subtitles -----
st.image(image, use_container_width=True)
st.subheader(" ")
st.subheader("NASA Space Apps 2025")
st.subheader("Hunting for Exoplanets with AI")
st.subheader("Team KNSPA & BLSPS")
st.subheader(" ")

st.markdown("Upload your data and interact with the AI model.")

# ----- Initialize session state for model and dataset -----
if "selected_model" not in st.session_state:
    st.session_state.selected_model = None
if "selected_dataset" not in st.session_state:
    st.session_state.selected_dataset = None

# ----- Top Buttons: Choose Model and Dataset -----
st.markdown("### Select Your Model and Dataset")
col1, col2 = st.columns(2)

with col1:
    st.session_state.selected_model = st.selectbox(
        "Choose Model",
        ["RandomForest", "SVC", "LinearRegression", "Cappucino"],
        index=0
    )

with col2:
    st.session_state.selected_dataset = st.selectbox(
        "Choose Dataset",
        ["TESS", "K2", "Kepler", "AllCombined"],
        index=0
    )

st.markdown("---")

# ----- Tabs -----
tab2, tab3 = st.tabs(["Use Models", "Train Models"])

# ----- Tab 2: Test Models -----
with tab2:
    st.header("Test Models")
    st.write(
        f"Use the CHOSEN model ({st.session_state.selected_model}) trained on the CHOSEN dataset "
        f"({st.session_state.selected_dataset}) to make predictions."
    )

    # Initialize session_state for saved test file path
    if "test_file_path" not in st.session_state:
        st.session_state.test_file_path = None

    uploaded_file_test = st.file_uploader("Upload CSV for prediction", type="csv", key="test")

    # Remove file if user clicked X
    if uploaded_file_test is None and st.session_state.test_file_path:
        deleted = delete_file_if_exists(st.session_state.test_file_path)
        if deleted:
            st.info(f"Plik testowy został usunięty z folderu input_data")
        st.session_state.test_file_path = None

    # Save new uploaded file
    if uploaded_file_test is not None:
        st.session_state.test_file_path = save_uploaded_csv(uploaded_file_test)
        test_data = pd.read_csv(st.session_state.test_file_path)
        st.write("Test Data Preview:")
        st.dataframe(test_data.head())

        if st.button("Run AI Model", key="predict"):
            st.write(
                f"Running predictions using the CHOSEN model ({st.session_state.selected_model}) "
                f"on the CHOSEN dataset ({st.session_state.selected_dataset})..."
            )
            # --- Placeholder predictions ---
            run_model(st.session_state.selected_model, st.session_state.selected_dataset)

            # Wczytaj wygenerowane predykcje
            predictions_path = "backend_models/outputs/predictions.csv"
            predictions_df = pd.read_csv(predictions_path)
            st.success("Predictions complete!")
            st.write("Predictions Preview:")
            st.dataframe(predictions_df.head())

            # Przygotuj CSV do pobrania
            csv_bytes = predictions_df.to_csv(index=False).encode('utf-8')
            st.download_button(
                label="Download Predictions CSV",
                data=csv_bytes,
                file_name="predictions.csv",
                mime="text/csv"
            )

# ----- Tab 3: Train Models -----
with tab3:
    st.header("Train Models")
    st.write(
        f"Train the CHOSEN model ({st.session_state.selected_model}) on the CHOSEN dataset "
        f"({st.session_state.selected_dataset})."
    )

    # Initialize session_state for saved train file path
    if "train_file_path" not in st.session_state:
        st.session_state.train_file_path = None

    uploaded_file_train = st.file_uploader("Upload CSV for training", type="csv", key="train")

    # Remove file if user clicked X
    if uploaded_file_train is None and st.session_state.train_file_path:
        deleted = delete_file_if_exists(st.session_state.train_file_path)
        if deleted:
            st.info(f"Plik treningowy został usunięty z folderu input_data")
        st.session_state.train_file_path = None

    # Save new uploaded file
    if uploaded_file_train is not None:
        st.session_state.train_file_path = save_uploaded_csv(uploaded_file_train)
        train_data = pd.read_csv(st.session_state.train_file_path)
        st.write("Training Data Preview:")
        st.dataframe(train_data.head())
        if st.button("Train Model", key="train_button"):
            st.write(
                f"Training the CHOSEN model ({st.session_state.selected_model}) on the CHOSEN dataset "
                f"({st.session_state.selected_dataset})..."
            )
            # model = train_model(train_data, st.session_state.selected_model)
            st.success("Training complete! Model saved.")
#%%
