#%%
import pandas as pd
import os
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
import joblib


clf = "../../saved-models/merged/optimal_rf.pkl"


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
    output_df.to_csv("predictions_with_prob.csv", index=False)

    return output_df

df = checkYourData()


df.head(10)

