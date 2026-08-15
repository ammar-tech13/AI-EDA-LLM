
# 📊 LLM-Powered Exploratory Data Analysis

An AI-powered Exploratory Data Analysis (EDA) application built with Python, Gradio, Pandas, Seaborn, Matplotlib, and Ollama.

## 🚀 Features

* Upload CSV datasets
* Automatic dataset summary
* Missing-value analysis
* Numerical and categorical data analysis
* Automatic histograms
* Correlation heatmap
* AI-generated insights using Mistral
* Interactive Gradio interface

## 🛠️ Technologies Used

* Python
* Pandas
* Matplotlib
* Seaborn
* Gradio
* Ollama
* Mistral LLM

## 📂 Project Structure

```text
EDA_LLM Integration/
│
├── app.py
├── titanic_ dataset_final.csv
├── requirements.txt
├── README.md
└── .gitignore
```

## ⚙️ Installation

Clone the repository:

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd "EDA_LLM Integration"
```

Install the required packages:

```bash
pip install -r requirements.txt
```

## 🤖 Ollama Setup

Install Ollama and download the Mistral model:

```bash
ollama pull mistral
```

Make sure Ollama is running before starting the application.

## ▶️ Run the Application

```bash
python app.py
```

The Gradio application will provide a local URL such as:

```text
http://127.0.0.1:7860
```

Open the URL in your browser.

## 🔄 Workflow

```text
Upload CSV
     ↓
Data Cleaning
     ↓
EDA Summary
     ↓
Missing Value Analysis
     ↓
Visualizations
     ↓
Mistral LLM
     ↓
AI-Generated Insights
```

## 📌 Example Dataset

The project includes a Titanic dataset for demonstrating the EDA workflow.

## 👨‍💻 Author

Ammar

## ⭐ Future Improvements

* Add more visualization types
* Add categorical-data visualizations
* Add downloadable EDA reports
* Add support for multiple LLM models
* Deploy the application online
