import numpy as np
import torch
from torch import nn
import matplotlib.pyplot as plt
from sklearn.metrics import precision_score, recall_score, f1_score, roc_auc_score
from sklearn.model_selection import StratifiedKFold
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
from pathlib import Path
import pandas as pd
import os

# ==========================================================
# Load and preprocess data
# ==========================================================

# X_train = np.loadtxt("../../datasets/merged/X_train_imputed_scaled.csv", delimiter=",", skiprows=1)
# X_test = np.loadtxt("../../datasets/merged/X_test_imputed_scaled.csv", delimiter=",", skiprows=1)
# y_train = np.loadtxt("../../datasets/merged/y_train.csv", delimiter=",", skiprows=1)
# y_test = np.loadtxt("../../datasets/merged/y_test.csv", delimiter=",", skiprows=1)
#
# # Delete ID column
# X_train = np.delete(X_train, 0, axis=1)
# X_test = np.delete(X_test, 0, axis=1)
# y_train = np.delete(y_train, 0, axis=1)
# y_test = np.delete(y_test, 0, axis=1)
#
# # Convert to tensors
# X_train = torch.from_numpy(X_train).float().squeeze()
# X_test = torch.from_numpy(X_test).float().squeeze()
# y_train = torch.from_numpy(y_train).float().squeeze()
# y_test = torch.from_numpy(y_test).float().squeeze()

device = "cuda" if torch.cuda.is_available() else "cpu"
print(f"Using device: {device}")

# ==========================================================
# Model definition
# ==========================================================

class ExoplanetsV0(nn.Module):
    def __init__(self, input_features, output_features, hidden_units=8):
        super().__init__()
        self.input_features = input_features
        self.output_features = output_features
        self.hidden_units = hidden_units

        self.layers = nn.Sequential(
            nn.Linear(input_features, hidden_units),
            nn.ReLU(),
            nn.Linear(hidden_units, hidden_units // 2),
            nn.ReLU(),
            nn.Linear(hidden_units // 2, hidden_units // 4),
            nn.ReLU(),
            nn.Linear(hidden_units // 4, output_features),
        )

    def forward(self, x):
        return self.layers(x)

# ==========================================================
# Accuracy function
# ==========================================================

def accuracy_fn(y_true, y_pred):
    correct = torch.eq(y_true, y_pred).sum().item()
    return (correct / len(y_pred)) * 100


# ==========================================================
# Saving and Loading models
# ==========================================================

MODEL_PATH = Path("backend_models/saved-models/nn")
MODEL_PATH.mkdir(parents=True, exist_ok=True)

def SaveModel(model, model_name: str):
    MODEL_SAVE_PATH = MODEL_PATH / f"{model_name}.pth"
    print(f"Saving model to: {MODEL_SAVE_PATH}")
    torch.save([model.state_dict(), model.input_features, model.output_features, model.hidden_units],
               f=MODEL_SAVE_PATH)

#SaveModel(model_1, "nn_exoplanets0")

def load_model(model_name):
    load = torch.load(MODEL_PATH / f"{model_name}.pth")
    model = ExoplanetsV0(load[1], load[2], load[3])
    model.load_state_dict(load[0])
    return model

# ==========================================================
# Predict new input data
# ==========================================================

feat_cols = ["period_d", "rp_re", "insol_eflux", "eq_temp", "teff_k", "logg_cgs", "rstar_rsun"]

def scaleAndInput(X_new):
    imputer = SimpleImputer(strategy='mean')
    X_new = pd.DataFrame(imputer.fit_transform(X_new), columns=feat_cols)
    scaler = StandardScaler()
    X_new = pd.DataFrame(scaler.fit_transform(X_new), columns=feat_cols)
    return X_new

def load_single_csv(folder_path="backend_models/input_data/"):
    csv_files = [f for f in os.listdir(folder_path) if f.endswith(".csv")]
    if len(csv_files) == 0:
        raise FileNotFoundError(f"Brak pliku CSV w folderze: {folder_path}")
    elif len(csv_files) > 1:
        raise ValueError(f"W folderze {folder_path} znaleziono więcej niż jeden plik CSV: {csv_files}")

    file_path = os.path.join(folder_path, csv_files[0])
    print(f"Wczytuję plik: {file_path}")

    data = pd.read_csv(file_path)
    data = data.drop(data.columns[0], axis=1)
    data = scaleAndInput(data)
    return torch.from_numpy(data.values).float().squeeze()

def use_model(model_name):
    model = load_model(model_name)
    model.eval()

    data = load_single_csv()
    with torch.inference_mode():
        logits = model(data)
        probs = torch.sigmoid(logits).squeeze()
        preds = (probs > 0.5).int()

        results = pd.DataFrame({
            "probability": probs.cpu().numpy(),
            "prediction": preds.cpu().numpy()
        })
        results.insert(0, "index", range(len(results)))
        output_path = "backend_models/outputs/predictions.csv"
        results.to_csv(output_path, index=False)

        print(f"Zapisano wyniki do pliku: {output_path}")
        print(results.head())

    folder = Path("backend_models/input_data")
    files = [f for f in folder.iterdir() if f.is_file()]
    if files:
        files[0].unlink()
        print(f"Usunięto plik: {files[0].name}")
    else:
        print("Folder jest pusty.")

# Example check
# use_model("nn_exoplanets0")
