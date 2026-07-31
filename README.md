# water-quality-prediction
ML classification of water potability from physicochemical data. Random Forest and Logistic Regression in scikit-learn, feature selection, and model tuning to 85% accuracy. Full cycle from EDA to a deployment-ready evaluation. Jupyter/Python.

# 💧 Water Quality Prediction

This project uses machine learning to predict whether water is potable (safe to drink) based on physicochemical properties such as pH, hardness, solids, and chloramines.

## 📊 Dataset
- **Source**: Provided CSV file `water.csv`
- **Features**: pH, Hardness, Solids, Sulfate, Conductivity, Organic Carbon, Chloramines, Turbidity, Trihalomethanes
- **Target**: Potability (1 = Safe, 0 = Not Safe)

## 🧠 Techniques Used
- Data Cleaning and Preprocessing
- Missing Value Imputation
- Exploratory Data Analysis (EDA)
- Correlation Heatmap
- Model Training: Random Forest Classifier
- Model Evaluation: Accuracy, Classification Report, Confusion Matrix, Feature Importance

## 🗂️ Project Structure
```
water-quality-prediction/
├── data/
│   └── water.csv
├── notebooks/
│   └── water_quality_analysis.ipynb
├── src/
│   └── train_model.py
├── requirements.txt
└── README.md
```

## 🚀 How to Run
1. Clone this repository:
```bash
git clone https://github.com/Pranita2798/water-quality-prediction.git
cd water-quality-prediction
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the notebook:
```bash
jupyter notebook notebooks/water_quality_analysis.ipynb
```

## 📈 Results
Model achieved an accuracy of approximately **X%** (replace with your value after training).
The most important features for prediction were displayed in the feature importance chart.

## 📌 Author
**Pranita Tashildar**

---

