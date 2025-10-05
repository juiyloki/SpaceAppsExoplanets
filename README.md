# SpaceAppsExoplanets
KN SPA &amp; BLSPS's project for Exoplanet Challenge for NASA Space Apps 2025.

## Key Contributions

* **Stacked Models**: We built and evaluated a stacking ensemble that combines the strengths of multiple machine learning algorithms to improve predictive accuracy.
* **Unified Dataset**: We created a new dataset by merging three publicly available sources: **Kepler**, **K2**, and **TESS** mission data. This allows for broader coverage, improved generalization, and a more robust evaluation of models.

## Project Goals

1. Compare the performance of different AI models in identifying exoplanet candidates.
2. Explore whether model stacking provides a measurable improvement over individual models.
3. Demonstrate the value of combining datasets from multiple missions into a single resource.

## Dataset

Our custom dataset is constructed from the following sources:

* [**Kepler Space Telescope**](https://exoplanetarchive.ipac.caltech.edu/cgi-bin/TblView/nph-tblView?app=ExoTbls&config=cumulative)
* [**K2 Mission**](https://exoplanetarchive.ipac.caltech.edu/cgi-bin/TblView/nph-tblView?app=ExoTbls&config=k2pandc)
* [**TESS (Transiting Exoplanet Survey Satellite)**](https://exoplanetarchive.ipac.caltech.edu/cgi-bin/TblView/nph-tblView?app=ExoTbls&config=TOI)

The preprocessing steps ensured consistency in labeling, normalization, and feature selection across all three sources.

## Models

We experimented with a range of models, including:

* Random Forest
* SVC
* Linear Regression
* Neural Networks

The stacked ensemble integrates predictions from these base learners to enhance accuracy.

## Results

* The stacking approach consistently outperformed individual models across several evaluation metrics.
* The combined data provides the largest known dataset for training.

## Web interface

How to start on localhost:

* Clone github repository: `git clone https://github.com/juiyloki/SpaceAppsExoplanets`
* Go to src folder: `cd src`
* Run streamlit: `streamlit run frontend/Home.py`
* App is ready on `http://localhost:8501`

## Acknowledgements

We thank NASA for making their data publicly available, enabling this research.

