#%%
import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
# from your_model_file import load_model, predict, train_model  # uncomment when ready

image = Image.open("pictures/logo.png")

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
tab1, tab2, tab3 = st.tabs(["Parse Data", "Test Models", "Train Models"])

# ----- Tab 1: Parse Data -----
with tab1:
    st.header("Parse Data")
    st.write(
        f"This tab allows you to parse your data according to the chosen model "
        f"({st.session_state.selected_model}) trained on the selected dataset "
        f"({st.session_state.selected_dataset})."
    )
    uploaded_file_parse = st.file_uploader("Upload CSV for parsing", type="csv", key="parse")
    if uploaded_file_parse is not None:
        data = pd.read_csv(uploaded_file_parse)
        st.write("Data Preview:")
        st.dataframe(data.head())
        st.write(f"Dataset shape: {data.shape}")
        st.write(
            f"Using model: {st.session_state.selected_model} trained on dataset: {st.session_state.selected_dataset}"
        )

# ----- Tab 2: Test Models -----
with tab2:
    st.header("Test Models")
    st.write(
        f"Use the CHOSEN model ({st.session_state.selected_model}) trained on the CHOSEN dataset "
        f"({st.session_state.selected_dataset}) to make predictions."
    )
    uploaded_file_test = st.file_uploader("Upload CSV for prediction", type="csv", key="test")
    if uploaded_file_test is not None:
        test_data = pd.read_csv(uploaded_file_test)
        st.write("Test Data Preview:")
        st.dataframe(test_data.head())

        if st.button("Run AI Model", key="predict"):
            st.write(
                f"Running predictions using the CHOSEN model ({st.session_state.selected_model}) "
                f"on the CHOSEN dataset ({st.session_state.selected_dataset})..."
            )
            # --- Placeholder predictions ---
            predictions = np.random.choice([0, 1], size=len(test_data))
            test_data['Predictions'] = predictions
            st.success("Predictions complete!")
            st.dataframe(test_data)

            # --- Prepare CSV for download ---
            csv = test_data.to_csv(index=False)
            st.download_button(
                label="Download Predictions CSV",
                data=csv,
                file_name=f"{st.session_state.selected_dataset}_{st.session_state.selected_model}_predictions.csv",
                mime="text/csv"
            )

# ----- Tab 3: Train Models -----
with tab3:
    st.header("Train Models")
    st.write(
        f"Train the CHOSEN model ({st.session_state.selected_model}) on the CHOSEN dataset "
        f"({st.session_state.selected_dataset})."
    )
    uploaded_file_train = st.file_uploader("Upload CSV for training", type="csv", key="train")
    if uploaded_file_train is not None:
        train_data = pd.read_csv(uploaded_file_train)
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

#%%
