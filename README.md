# 🚖 Big Data Analysis Using PySpark — NYC Yellow Taxi Trip Data

## 🔍 Overview
This project demonstrates large-scale data analysis using PySpark on the **NYC Yellow Taxi trip dataset (January 2023)** in **Parquet format**. It includes real-time aggregation, statistical insights, and professional data visualizations.

## 📁 Dataset
- **Format**: `.parquet`
- **Size**: ~3 million records
- **Fields**: Pickup time, dropoff time, fare amount, trip distance, locations, etc.

## 🧰 Tools Used
- [PySpark 4.0.0](https://spark.apache.org/)
- [Pandas](https://pandas.pydata.org/)
- [Seaborn](https://seaborn.pydata.org/)
- [Matplotlib](https://matplotlib.org/)

## 📊 Key Insights Extracted
- **Peak pickup hours**: 5 PM – 8 PM
- **Most popular pickup zone**: Location ID `132`
- **Average trip distance**: ~3.85 miles
- **Fare spikes**: Early mornings around 5–6 AM

## 📈 Visualizations
- 📌 Bar chart of **trips by hour**
- 🚕 Top 10 **pickup locations**
- 💵 Line chart of **average fare by hour**

Charts are auto-saved as PNGs:
trips_by_hour.png
top_pickups.png
fare_by_hour.png


## 🔧 How to Run 
   install python 3.9 / 3.13 
### Prerequisites
Install  dependencies: through windows powershell / cmd / vs terminal 
```bash
pip install -r requirements.txt
## Run the code 

File structure 
  mainfolder/
├── yellow_tripdata_2023-01.parquet
├── big_data_analysis_with_charts.py
├── requirements.txt
├── README.md
├── trips_by_hour.png
├── top_pickups.png
├── fare_by_hour.png

Author : SANJAY K 2025