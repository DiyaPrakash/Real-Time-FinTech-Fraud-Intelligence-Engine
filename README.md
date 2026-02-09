# 💳 Real-Time FinTech Fraud Intelligence Platform

An end-to-end Machine Learning system for **real-time fraud detection**, built using open-source technologies.  
This project simulates a production-style fintech fraud monitoring platform with API services, live dashboards, and explainable AI.

---

## 🚀 Project Overview

Financial fraud detection is a critical challenge due to:

- Extreme class imbalance  
- Evolving fraud patterns  
- Need for real-time decisions  
- Requirement for explainability  

This project demonstrates a complete ML lifecycle — from raw data analysis to deployment and monitoring.

---

## 🧠 Key Features

- Exploratory Data Analysis on multiple datasets  
- Feature engineering and preprocessing pipeline  
- Machine learning model training and evaluation  
- Real-time synthetic transaction simulator  
- FastAPI prediction service  
- Interactive Streamlit dashboard  
- Transaction history logging  
- Manual & automated transaction testing  
- Explainable AI using SHAP  
- End-to-end open-source stack  

---


## 📊 Datasets Used

### 1. Credit Card Fraud Dataset
- Clean, numeric dataset  
- Used for baseline modeling  
- Ideal for learning fraud patterns  

### 2. IEEE-CIS Fraud Dataset
- Large, complex, real-world dataset  
- Mixed data types and missing values  
- Used for advanced modeling and scalability testing  

---

## 🛠️ Tech Stack

| Layer | Technology |
|------|------------|
| Language | Python |
| ML Models | Scikit-learn, XGBoost |
| Data Handling | Pandas, NumPy |
| API | FastAPI |
| Dashboard | Streamlit |
| Explainability | SHAP |
| Visualization | Matplotlib, Seaborn |
| Serialization | Joblib |
| Deployment | Uvicorn |
| Version Control | Git |

All tools are **free and open-source**.

---


## ▶️ How to Run

### 1. Install Dependencies
pip install -r requirements.txt

---

### 2. Start API Server
uvicorn api.app:app --reload

---

### 3. Start Dashboard
streamlit run dashboard/app.py

---

### 4. Optional — Run Simulator
python simulator/generator.py


---

## 📈 Dashboard Capabilities

- Manual transaction input  
- Random transaction generation  
- Fraud probability visualization  
- SHAP feature influence charts  
- Transaction history table  
- Real-time API integration  

---

## 🔍 Explainable AI

The system uses **SHAP (SHapley Additive exPlanations)** to:

- Identify top influencing features  
- Increase model transparency  
- Support trust and decision-making  
- Simulate real-world fintech compliance needs  

---

## 📌 Evaluation Metrics

- ROC-AUC  
- Precision-Recall AUC  
- Recall (Fraud Detection Rate)  
- Confusion Matrix  
- Feature Importance  

---

## 🔮 Future Improvements

- User authentication  
- Email/SMS fraud alerts  
- Model drift monitoring  
- Docker deployment  
- Multi-model comparison  
- Real payment gateway integration  

---

## 📜 License

Open-source for educational and research purposes.

---

## 🙌 Acknowledgements

- Kaggle datasets  
- Open-source ML community  
- FastAPI & Streamlit contributors  

---

## 💡 Final Note

This project demonstrates not only machine learning skills but also **system design, API integration, explainable AI, and product-level thinking**, bridging the gap between academic ML and real-world deployment.


