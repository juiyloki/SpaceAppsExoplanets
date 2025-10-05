import pandas as pd
import numpy as np
import importlib.util
from pathlib import Path

path_to_module = Path("backend/models/neural-networks/KeplerNN.ipynb")
spec = importlib.util.spec_from_file_location("KeplerNN", path_to_module)
KeplerNN = importlib.util.module_from_spec(spec)
spec.loader.exec_module(KeplerNN)

def run_model(selected_model: str, selected_dataset: str):
    # Kombinacja Cappucino + AllCombined -> wywołanie neural network
    if selected_model == "Cappucino" and selected_dataset == "AllCombined":
        predictions = KeplerNN.use_model("nn_exoplanets_0")
    else:
        # placeholder dla innych modeli
        print("This combination of model and dataset is not supported right now.")

