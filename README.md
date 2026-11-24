🏠 California House Price Predictor

A containerized machine learning web application built with **FastAPI**, **Jinja2**, **Joblib**, and **Docker** that estimates California house prices based on property, demographic, and location features.

---

## ✨ Features

- **Real-Time ML Predictions:** Serves predictions from a serialized scikit-learn model (`california.joblib`) using NumPy.
- **Interactive Web Interface:** Clean HTML/CSS frontend rendered via Jinja2 templates (`templates/index.html`) and static assets (`/static`)[cite: 1].
- **Input Validation & State Preservation:** Validates empty fields, numeric formatting, and finite values (`NaN`/`inf`), while preserving user-entered values on form submission[cite: 1].
- **Dockerized Setup:** Includes a `Dockerfile` based on `python:3.11-slim` for consistent local and cloud deployment[cite: 1].

---

## 🛠️ Tech Stack

- **Backend:** Python 3.11, FastAPI, Uvicorn[cite: 1]
- **Frontend:** Jinja2 Templates, HTML/CSS[cite: 1]
- **Machine Learning:** NumPy, Joblib, scikit-learn[cite: 1]
- **Containerization:** Docker[cite: 1]

---

## 📂 Project Structure

```text
├── app.py                 # FastAPI application and prediction route
├── california.joblib      # Serialized ML model and feature columns
├── Dockerfile             # Docker image configuration
├── requirements.txt       # Python dependencies
├── static/                # Static assets (CSS, images, etc.)
└── templates/
    └── index.html         # Frontend web form and result display
```[cite: 1]

---

## 📊 Input Features

| Feature | Label | Description |
| :--- | :--- | :--- |
| `MedInc` | Median Income | Median income of households[cite: 1] |
| `HouseAge` | House Age | Median age of houses[cite: 1] |
| `AveRooms` | Average Rooms | Average number of rooms[cite: 1] |
| `AveBedrms` | Average Bedrooms | Average bedrooms[cite: 1] |
| `Population` | Population | Area population[cite: 1] |
| `AveOccup` | Average Occupancy | Average household occupancy[cite: 1] |
| `Latitude` | Latitude | Geographical latitude[cite: 1] |
| `Longitude` | Longitude | Geographical longitude[cite: 1] |

---

## 🚀 Getting Started

### Option 1: Run Locally with Python

1. **Clone the repository**
   ```bash
   git clone <your-github-repo-url>
   cd <your-repo-folder>
