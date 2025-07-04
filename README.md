# 🔥 Global AI Salary Prediction API with FastAPI

This is an end-to-end Machine Learning project that predicts salaries in the AI industry using key job features such as age, department, overtime status, job satisfaction, and more. It uses the [Global AI Job Trends and Salary Insights](https://www.kaggle.com/datasets/promptcloud/global-ai-job-trends-and-salary-insights) dataset and is deployed using **FastAPI**.

## 📁 Project Structure

📦 SalaryPredictionAPI
├── main.py # FastAPI application with /predict endpoint
├── xgb_model.pkl # Trained XGBoost model
├── feature_names.pkl # Ordered list of features used in training
├── requirements.txt # Project dependencies
└── README.md # Project documentation

yaml
Copy
Edit

---

## 🎯 Features

- Cleaned and processed real-world AI job dataset from Kaggle
- Feature selection and model training using XGBoost Regressor
- Deployed as an API using FastAPI with Swagger UI for testing
- Takes JSON input and returns predicted salary in real-time

---

## 🚀 Getting Started

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/yourusername/ai-salary-predictor-api.git
cd ai-salary-predictor-api
2️⃣ Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
3️⃣ Run the FastAPI App
bash
Copy
Edit
uvicorn main:app --reload
4️⃣ Visit API Docs
Navigate to http://127.0.0.1:8000/docs to test the API.

🧪 Sample Request Body
json
Copy
Edit
{
  "Age": 29,
  "Gender": "Female",
  "Department": "Sales",
  "JobLevel": 2,
  "MonthlyIncome": 4500,
  "OverTime": "Yes",
  "WorkLifeBalance": 2,
  "JobSatisfaction": 4,
  "YearsAtCompany": 3
}
📤 Sample Response
json
Copy
Edit
{
  "prediction": 77472.69
}
📦 Built With
XGBoost – High-performance model for regression

FastAPI – Fast, asynchronous API framework

Pandas & NumPy – Data manipulation

Joblib – Model and feature serialization

Uvicorn – ASGI server for FastAPI

📈 Why This Project?
✅ Demonstrates real-world ML deployment
✅ Perfect for ML Engineer / Data Scientist portfolio
✅ Easily extensible (frontend, Docker, cloud deployment)

🧠 Author
Dilrabo Khidirova
🎓 Master's in Software Engineering (AI & Data Track)
🌐 LinkedIn
🚀 Passionate about real-world AI applications and deployment

📌 Next Steps
✅ Add unit tests

✅ Deploy on Render/Heroku

🔜 Add Streamlit frontend for public interaction

🔜 Monitor usage with Prometheus/Grafana