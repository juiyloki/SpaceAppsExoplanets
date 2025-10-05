import importlib.util
import os
from pathlib import Path
import torch

import joblib
import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler


def load_kepler_module():
    """
    Dynamicznie ładuje moduł KeplerNN z pliku .py.
    Zwraca zaimportowany moduł.
    """
    # Upewnij się, że ścieżka wskazuje na plik .py (nie .ipynb)
    path_to_module = Path("backend_models/models/neural-networks/KeplerNN.py").resolve()

    if not path_to_module.exists():
        raise FileNotFoundError(f"Nie znaleziono pliku modułu: {path_to_module}")

    spec = importlib.util.spec_from_file_location("KeplerNN", path_to_module)
    KeplerNN = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(KeplerNN)
    return KeplerNN


def run_model(selected_model: str, selected_dataset: str):
    """
    Uruchamia wybrany model w zależności od przekazanych parametrów.
    """

    if selected_model == "Cappucino (Neural Network)" and selected_dataset == "AllCombined":
        print("🔭 Uruchamianie modelu Cappucino (AllCombined)...")
        KeplerNN = load_kepler_module()
        KeplerNN.use_model("neural_network_01")  # dopasowane do Twojego zapisu modelu
    else:
        print(f"❌ Ta kombinacja ({selected_model}, {selected_dataset}) nie jest jeszcze wspierana.")

    if __name__ == "__main__":
        run_model("Cappucino", "AllCombined")

    if selected_model == "RandomForest" and selected_dataset == "AllCombined":
        clf_id = "backend_models/saved-models/merged/optimal_rf.pkl"
        checkYourData()




clf = "backend_models/saved-models/merged/optimal_rf.pkl"


feat_cols = [
    "period_d", "rp_re", "insol_eflux", "eq_temp", "teff_k", "logg_cgs", "rstar_rsun"
]

def scaleAndInput(X_new):
    imputer = SimpleImputer(strategy='mean')
    X_new = pd.DataFrame(imputer.fit_transform(X_new), columns=feat_cols)

    scaler = StandardScaler()
    X_new = pd.DataFrame(scaler.fit_transform(X_new), columns=feat_cols)

    return X_new


def checkYourData(folder_path="input_data"):

    csv_files = [f for f in os.listdir(folder_path) if f.endswith(".csv")]

    if len(csv_files) == 0:
        raise FileNotFoundError(f" Brak pliku CSV w folderze: {folder_path}")
    elif len(csv_files) > 1:
        raise ValueError(f"W folderze {folder_path} znaleziono więcej niż jeden plik CSV: {csv_files}")

    file_path = os.path.join(folder_path, csv_files[0])
    print(f" Wczytuję plik: {file_path}")

    data = pd.read_csv(file_path)
    data = data.drop(data.columns[0], axis=1)

    data = scaleAndInput(data)

    X_new = data

    clf = joblib.load("saved-models/merged/optimal_voting_rf_svc.pkl")

    y_proba = clf.predict_proba(X_new)[:, 1]

    y_pred = (y_proba >= 0.4).astype(int)

    output_df = pd.DataFrame({
        "id": X_new.index,
        "prediction": y_pred,
        "probability": y_proba
    })
    output_df.to_csv("backend_modules/outputs/predictions.csv", index=False)

    return output_df