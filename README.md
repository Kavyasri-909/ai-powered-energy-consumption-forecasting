# ⚡ AI-Powered Energy Consumption Forecasting System

---

## 📌 Problem Statement

Energy consumption is a critical factor in modern infrastructure, including smart homes, industries, and power grids.
Unoptimized energy usage leads to:

* Increased operational costs
* Energy wastage
* Inefficient resource allocation
* Grid instability

There is a need for a system that can **predict future energy consumption** based on historical usage patterns and time-based features.

---

## 💡 Solution Approach

This project builds an **AI-powered forecasting system** using Machine Learning to predict energy consumption.

### 🔹 Workflow:

1. **Data Collection**

   * Used publicly available energy consumption dataset

2. **Data Preprocessing**

   * Converted timestamps into structured features:

     * Hour
     * Day
     * Month
   * Handled missing values

3. **Feature Engineering**

   * Extracted time-based patterns
   * Prepared dataset for training

4. **Model Training**

   * Used **Random Forest Regressor**
   * Split data into training and testing sets

5. **Prediction System**

   * Built prediction pipeline for real-time input

6. **Deployment**

   * Developed an interactive dashboard using **Streamlit**

---

## 🛠️ Tech Stack

| Category             | Tools Used    |
| -------------------- | ------------- |
| Programming Language | Python        |
| Data Processing      | Pandas, NumPy |
| Machine Learning     | Scikit-learn  |
| Visualization        | Matplotlib    |
| Deployment           | Streamlit     |
| Version Control      | Git, GitHub   |

---

## 📊 Features

* 📈 Energy consumption prediction
* ⏱ Time-based forecasting (hour/day/month)
* 🌐 Interactive web interface
* ⚡ Fast predictions using trained ML model

---

## 📸 Screenshots

> Add screenshots after running the app:

* Home page of Streamlit app
* Prediction output
* Graphs (if added)

Example:

![App Screenshot](screenshots/app.png)

---

## ⚙️ How to Run the Project

### 🔹 Step 1: Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/energy-forecasting-ai.git
cd energy-forecasting-ai
```

---

### 🔹 Step 2: Create Virtual Environment (Recommended)

```bash
python -m venv venv
```

Activate:

**Windows:**

```bash
venv\Scripts\activate
```

**Mac/Linux:**

```bash
source venv/bin/activate
```

---

### 🔹 Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 🔹 Step 4: Add Dataset

* Place dataset inside:

```
data/raw/energy.csv
```

---

### 🔹 Step 5: Train the Model

```bash
python src/train_model.py
```

This will generate:

```
models/model.pkl
```

---

### 🔹 Step 6: Run Streamlit App

```bash
cd app
streamlit run streamlit_app.py
```

---

### 🔹 Step 7: Open in Browser

Streamlit will automatically open:

```
http://localhost:8501
```

---

## 🚀 Future Improvements

* 📊 Add LSTM / Deep Learning models
* 🌦 Integrate weather data
* 📅 Forecast next 7 days
* ☁️ Deploy on cloud (AWS / Azure)
* 📉 Advanced visualization dashboard

---

## 📌 Project Highlights

* Built end-to-end ML pipeline
* Designed interactive UI
* Simulated real-world energy system
* Production-style project structure

---

## 👨‍💻 Author
GitHub: https://github.com/kavyasri-909


---
