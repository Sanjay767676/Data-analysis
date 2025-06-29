import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from nltk.corpus import stopwords
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
import nltk
nltk.download('stopwords')

# Load Dataset
df = pd.read_csv("Tweets.csv")
print("✅ Dataset loaded successfully.\n")

# Dataset Info
print("📊 Dataset Info:")
print(df.info())
print()

# Check missing values
print("🔍 Missing Values:")
print(df.isnull().sum())
print()

# Sentiment Distribution
print("🧾 Sentiment Label Distribution:")
print(df['airline_sentiment'].value_counts())
print()

# 🔽 Plotting Sentiment Distribution
plt.figure(figsize=(8, 6))
ax = sns.countplot(data=df, x='airline_sentiment', hue='airline_sentiment', palette='Set2', legend=False)
for p in ax.patches:
    ax.annotate(f'{p.get_height()}', (p.get_x() + p.get_width() / 2., p.get_height()),
                ha='center', va='center', fontsize=10, color='black', xytext=(0, 8),
                textcoords='offset points')
plt.title("Sentiment Distribution of Airline Tweets", fontsize=14)
plt.xlabel("Sentiment")
plt.ylabel("Tweet Count")
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig("sentiment_distribution.png")  # Saves plot as PNG
plt.show()

# Preprocessing
stop_words = set(stopwords.words("english"))
df['clean_text'] = df['text'].apply(
    lambda x: ' '.join([word for word in x.lower().split() if word not in stop_words])
)

# Feature and target
X = df['clean_text']
y = df['airline_sentiment']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# TF-IDF
vectorizer = TfidfVectorizer(max_features=5000)
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

# Model Training
model = LogisticRegression(max_iter=1000)
model.fit(X_train_vec, y_train)

# Predictions
y_pred = model.predict(X_test_vec)

# Evaluation
print("📋 Classification Report:")
print(classification_report(y_test, y_pred))
print()

print("🔢 Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))
print()

print(f"🎯 Accuracy Score: {accuracy_score(y_test, y_pred):.2f}")
