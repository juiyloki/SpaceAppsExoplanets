import importlib.util
from pathlib import Path

def load_kepler_module():
    """
    Dynamicznie ładuje moduł KeplerNN z pliku .py.
    Zwraca zaimportowany moduł.
    """
    # Upewnij się, że ścieżka wskazuje na plik .py (nie .ipynb)
    path_to_module = Path("backend/models/neural-networks/KeplerNN.py").resolve()

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
    KeplerNN = load_kepler_module()

    if selected_model == "Cappucino" and selected_dataset == "AllCombined":
        print("🔭 Uruchamianie modelu Cappucino (AllCombined)...")
        KeplerNN.use_model("nn_exoplanets0")  # dopasowane do Twojego zapisu modelu
    else:
        print(f"❌ Ta kombinacja ({selected_model}, {selected_dataset}) nie jest jeszcze wspierana.")

    if __name__ == "__main__":
        run_model("Cappucino", "AllCombined")
