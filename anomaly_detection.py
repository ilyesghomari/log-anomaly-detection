from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler
import numpy as np

# Simulated log data
X = np.random.rand(1000, 5)

# Preprocessing
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Model
model = IsolationForest(n_estimators=100, contamination=0.05, random_state=42)
model.fit(X_scaled)

# Prediction
preds = model.predict(X_scaled)
print(preds)
