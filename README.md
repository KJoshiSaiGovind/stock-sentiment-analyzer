# 📈 Real-Time Stock Sentiment Analyzer

A machine learning-based web application that performs **sentiment analysis** on stock market-related news headlines and tweets to determine whether the sentiment is **positive, negative, or neutral**.  
This project helps investors and traders get real-time insights into market sentiment before making decisions.

---

## 🚀 Features
- Load and preprocess stock market news dataset
- Perform **Exploratory Data Analysis (EDA)**
- Train ML models (Logistic Regression, Random Forest, Naive Bayes, etc.)
- Visualize model performance with charts
- Real-time stock sentiment classification via web app (Flask/Streamlit)

---

## 📂 Project Structure
stock-sentiment-analyzer/
│── data/
│ └── all-data.csv # Dataset file
│
│── notebooks/
│ └── EDA_notebook.ipynb # Exploratory Data Analysis
│
│── app.py # Main web application file
│── visualize.py # Data visualization functions
│── requirements.txt # Required dependencies
│── README.md # Project documentation

---

## 🛠 Installation & Setup
1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/stock-sentiment-analyzer.git
   cd stock-sentiment-analyzer

2.Create and activate a virtual environment:
python -m venv venv
# On Windows
venv\Scripts\activate
# On Mac/Linux
source venv/bin/activate

3.Install Dependencies
pip install -r requirements.txt

4.Place the dataset inside the data/ folder:
data/all-data.csv

5.Run EDA (optional but recommended):
jupyter notebook notebooks/EDA_notebook.ipynb

6.Start the application:
python app.py

📊 Example Output

Input: "Stock prices are expected to rise after the latest earnings report"

Output: Positive

Input: "The market crashed due to global uncertainty"

Output: Negative

📌 Requirements

Python 3.8+

pandas

numpy

scikit-learn

matplotlib / seaborn

Flask or Streamlit

NLTK / TextBlob

Install all with:

pip install -r requirements.txt

📖 Future Enhancements

Add deep learning (LSTM/BERT) for improved sentiment accuracy

Live integration with Twitter API and Yahoo Finance

Interactive dashboard with Plotly/Dash

🙌 Author

👤 Karri Joshi Sai Govind

📧 karrisaigovind33@gmail.com

🔗 LinkedIn

💻 GitHub