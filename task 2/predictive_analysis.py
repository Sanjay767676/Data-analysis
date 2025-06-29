import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
import seaborn as sns
import matplotlib.pyplot as plt

# Step 1: Load dataset
df = pd.read_csv('diabetes.csv')
print("✅ Dataset loaded successfully.")

# Step 2: Basic exploration
print("\n📊 Dataset Info:")
print(df.info())

print("\n🔍 Missing Values:")
print(df.isnull().sum())

print("\n📈 Statistical Summary:")
print(df.describe())

# Step 3: Correlation Heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
plt.title('Feature Correlation Heatmap')
plt.tight_layout()
plt.savefig("correlation_heatmap.png")
plt.close()

# Step 4: Feature selection & target
X = df.drop('Outcome', axis=1)
y = df['Outcome']

# Step 5: Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 6: Scale features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Step 7: Train model
model = RandomForestClassifier(random_state=42)
model.fit(X_train_scaled, y_train)
print("✅ Model training complete.")

# Step 8: Predict
y_pred = model.predict(X_test_scaled)

# Step 9: Evaluate
print("\n📋 Classification Report:")
print(classification_report(y_test, y_pred))

print("🔢 Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))

print("🎯 Accuracy Score:", accuracy_score(y_test, y_pred))

# Step 10: Feature Importance Plot
feature_importance = pd.Series(model.feature_importances_, index=X.columns)
feature_importance.sort_values().plot(kind='barh', figsize=(8, 6))
plt.title("Feature Importance")
plt.tight_layout()
plt.savefig("feature_importance.png")
plt.close()
