# 📘 Data Analysis Internship Tasks

This project contains three tasks completed during the CodTech Data Analysis internship.

---
> this symbol indicates commed to be run in vs terminal 
## ✅ Prerequisites

☑️ **Install Visual Studio Installer Components**  
Make sure Visual Studio Installer is installed with:

- `C++ Build Tools`
- `Windows SDK (basic required build tools)`

 🛠️ This is needed for compiling Python packages that rely on native extensions.

---

## 🐍 Python Installation

Ensure one of the following Python versions is installed:

- Python `3.10`
- Python `3.13` (if available)

Verify installation:
   
    python --version 

### 🧪 Setting Up Virtual Environment
Create a virtual environment for Python 3.10:

    python -m venv venv310 
### Activate the virtual environment (PowerShell):
    .\venv310\Scripts\Activate.ps1

### If you face execution policy issues:

    Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
### Then re-run:
    .\venv310\Scripts\Activate.ps1

 ### After activating the virtual environment:

📦 Installing Required Packages

    pip install -r requirements.txt

### Make sure requirements.txt is in the root of your project.

🧠 Running Tasks (VS Code)
📌 Important: Open dedicated terminal in VS Code for each task.

### ▶️ Task 1: Big Data Analysis

    cd task 1
  
     python big_data_analysis.py

### ▶️ Task 2: Diabetes Prediction

     cd task 2
  
     python predictive_analysis.py

### ▶️ Task 3: Sentiment Analysis (Tweets)

## *Make sure Tweets.csv is in the same directory as the script.*

    cd task 4
  
     python sentiment_analysis.py

### 📁 Folder Structure
data-analysis/
│
├── task 1/
│   └── big_data_analysis.py
│
├── task 2/
│   ├── diabetes.csv
│   └── predictive_analysis.py
│
├── task 4/
│   ├── Tweets.csv
│   └── sentiment_analysis.py
│
├── requirements.txt
└── README.md

