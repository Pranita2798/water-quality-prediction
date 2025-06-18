import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pickle

# Load data
df = pd.read_csv('data/water_quality.csv')

# Features and target
features = ['ph', 'do', 'turbidity']  # Update as per your dataset
target = 'wqi_class'

X = df[features]
y = df[target]

# Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Save model
with open('models/model.pkl', 'wb') as f:
    pickle.dump(model, f)

# Feature Importance
importances = model.feature_importances_
print("✅ Model trained and saved to 'models/model.pkl'")
print("\n🔍 Feature Importances:")
for feature, score in zip(features, importances):
    print(f"{feature}: {score:.4f}")
