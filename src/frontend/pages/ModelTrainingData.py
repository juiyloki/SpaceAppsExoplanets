import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# --- Pełny ekran ---
st.set_page_config(
    page_title="Exoplanet Visualization Dashboard",
    layout="wide",  # bardzo ważne, żeby wykorzystać całą szerokość
)

st.title("📊 Exoplanet Data Visualization Dashboard")
st.write("Explore, visualize, and describe data insights in three sections below.")
st.markdown("---")

# ---- 3 SECTIONS (columns) ----
col1, col2, col3 = st.columns(3, gap="large")

# ======= COLUMN 1 =======
with col1:
    st.subheader("🌍 Gotowy wykres")
    st.write("Opis wykresu np. liczba odkryć w czasie.")

    # Większy wykres
    x = np.linspace(0, 10, 100)
    y = np.sin(x)
    fig, ax = plt.subplots(figsize=(6, 4))  # większy rozmiar
    ax.plot(x, y, label="sin(x)", linewidth=2)
    ax.set_title("Gotowy wykres sin(x)", fontsize=14)
    ax.set_xlabel("x", fontsize=12)
    ax.set_ylabel("y", fontsize=12)
    ax.legend()
    st.pyplot(fig)

# ======= COLUMN 2 =======
with col2:
    st.subheader("🪐 Wykres korelacji")
    st.write("Porównanie losowych danych.")

    np.random.seed(42)
    x2 = np.random.rand(50)
    y2 = np.random.rand(50)
    fig2, ax2 = plt.subplots(figsize=(6, 4))
    ax2.scatter(x2, y2, color="orange", s=70, alpha=0.7)
    ax2.set_title("Przykładowy scatter plot", fontsize=14)
    ax2.set_xlabel("X", fontsize=12)
    ax2.set_ylabel("Y", fontsize=12)
    st.pyplot(fig2)

# ======= COLUMN 3 =======
with col3:
    st.subheader("⭐ Histogram")
    st.write("Rozkład losowych wartości.")

    data3 = np.random.normal(0, 1, 200)
    fig3, ax3 = plt.subplots(figsize=(6, 4))
    ax3.hist(data3, bins=20, color="skyblue", edgecolor="black")
    ax3.set_title("Histogram losowych wartości", fontsize=14)
    ax3.set_xlabel("Wartość", fontsize=12)
    ax3.set_ylabel("Częstość", fontsize=12)
    st.pyplot(fig3)
