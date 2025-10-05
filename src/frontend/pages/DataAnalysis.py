# pages/2_DataAnalysis.py
import streamlit as st
from pathlib import Path
from PIL import Image

# ----- CSS dla stylu kosmicznego -----
st.markdown("""
<style>
/* Tło całej strony */
body {
    background: linear-gradient(to bottom, #0b0c2a, #1a1a40, #000000);
    color: white;
}

/* Glow effect dla tytułów wykresów */
.glow-title {
    color: #39ff14;
    font-weight: bold;
    text-shadow: 0 0 5px #39ff14, 0 0 10px #39ff14, 0 0 15px #39ff14;
}

/* Box wokół obrazka */
.plot-box {
    background-color: rgba(10,10,30,0.7);
    padding: 10px;
    margin-bottom: 20px;
    border-radius: 10px;
    box-shadow: 0 0 10px #00f0ff;
}

/* Podpis i opis */
.plot-caption {
    font-size: 16px;
    margin-top: 5px;
}
</style>
""", unsafe_allow_html=True)

# ----- Nagłówek strony -----
st.title("🌌 Data Analysis Portal")
st.markdown("Explore exoplanet detection data in **Open Source** and **Neural Network** workflows.")
st.markdown("---")

# ----- Foldery z obrazkami -----
# Foldery dla zakładek Open Source
open_source_merged_folder = Path("pictures/data_analysis/open_source/merged")
open_source_kepler_folder = Path("pictures/data_analysis/open_source/kepler")

# Folder Neural Network
nn_folder = Path("pictures/data_analysis/neural_network")

# ----- Dwukolumnowy układ -----
col1, col2 = st.columns(2)

# ----- Lewa kolumna: Open Source -----
with col1:
    st.header("🪐 Open Source")

    tab_merged, tab_kepler = st.tabs(["Dataset Merged", "Kepler"])

    with tab_merged:
        st.write("Tutaj wyświetlamy wykresy Dataset Merged")
        # pętla po obrazkach Merged
        for img_path in sorted(open_source_merged_folder.glob("*.*")):
            st.image(img_path, use_column_width=True)
            st.markdown(f"🚀 {img_path.stem}")
            st.markdown(f"Opis wykresu {img_path.stem}")

    with tab_kepler:
        st.write("Tutaj wyświetlamy wykresy Kepler")
        for img_path in sorted(open_source_kepler_folder.glob("*.*")):
            st.image(img_path, use_column_width=True)
            st.markdown(f"🚀 {img_path.stem}")
            st.markdown(f"Opis wykresu {img_path.stem}")

# ----- Prawa kolumna: Neural Network -----
with col2:
    st.header("🤖 Neural Network")
    for img_path in sorted(nn_folder.glob("*.*")):
        st.markdown('<div class="plot-box">', unsafe_allow_html=True)
        image = Image.open(img_path)
        st.image(image, use_column_width=True)
        st.markdown(f'<p class="glow-title">🛸 {img_path.stem}</p>', unsafe_allow_html=True)
        st.markdown(f'<p class="plot-caption">Opis wykresu {img_path.stem} w Neural Network workflow.</p>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

st.markdown("---")
st.info("Każdy box ma swoje miejsce i odstępy, glow effect tytułów oraz kosmiczne emoji przy podpisach ✨")
