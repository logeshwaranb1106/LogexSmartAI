# LogexSmartAI
# 🤖 LogexSmartAI – Real-Time Stock Sentiment & News Analyzer

**LogexSmartAI** is a lightweight, interactive web application built using **Streamlit** and powered by **Google's Gemini 2.5 Flash model**. It allows users to type in the name of a stock (scrip), and instantly receive a detailed analysis of the stock's sentiment, current standing, recent news, and analyst expectations.

## 🚀 Features

- 📈 Real-time sentiment analysis of user-typed stock scrips
- 🧠 Powered by Google Gemini 2.5 Flash for natural language understanding
- 📰 Summarizes the latest 10 impactful financial news items
- 📊 Stock outlook, health, and analyst sentiment table
- 🧪 Identifies stocks needing further review and suggests focus areas
- 💻 Clean and modern UI using Streamlit
- 🖼️ Circular profile logo for clean branding

## 🖼️ App Preview

![LogexSmartAI Screenshot](your-screenshot-path.png)

---

## 🧠 How It Works

1. User types a stock name (scrip) in the sidebar.
2. The app dynamically builds a detailed prompt for the Gemini model.
3. Gemini generates:
   - Portfolio health status
   - Table of stock sentiment
   - List of stocks that need further review
   - Latest 10 important news events
4. The app displays results in a clean, readable format.

---

## ⚙️ Tech Stack

- [Streamlit](https://streamlit.io/)
- [Google Generative AI (Gemini 2.5 Flash)](https://ai.google.dev/)
- Python 3.10+
- Custom Prompt Engineering

---

## 🏁 Getting Started

### 🔧 Prerequisites

- Python 3.10+
- Gemini API Key from [Google AI Studio](https://makersuite.google.com/app)

### 📥 Installation

```bash
git clone https://github.com/your-username/logexsmartai-sentiment-analyzer.git
cd logexsmartai-sentiment-analyzer
pip install -r requirements.txt

---

Live Deployment
- https://logexsmartai.onrender.com
