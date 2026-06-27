# STATIFY 2.0 - Financial Analyst Chatbot

## Team Name

QuadCore

## Team Members

* Saaketha Surya Jeevanigi
* Anudeep Makam
* Anreddy Spurthi
* Mannem Yashasvi

---

# Project Overview

This project is an LLM-powered Financial Analyst Chatbot built for the STATIFY 2.0 Week-1 GenAI Task.

The chatbot can:

* Fetch real-time stock prices using Yahoo Finance
* Retrieve the latest company-related financial news using DuckDuckGo Search
* Generate conversational responses using a Hugging Face open-source language model

---

# Project Architecture

The project is divided into three main files:

## 1. Week1.py

This is the main execution file.

Responsibilities:

* Runs the chatbot loop
* Accepts user input
* Coordinates interactions between the LLM and tools

## 2. tool.py

Contains all external tools used by the chatbot.

Implemented Tools:

* Stock Price Tool using `yfinance`
* News Search Tool using `DuckDuckGo Search`

## 3. schema.py

Defines structured data models using Pydantic.

Responsibilities:

* Input validation
* Structured request/response formatting

---

# Technologies Used

* Python
* Hugging Face Transformers
* LangChain
* yFinance
* DuckDuckGo Search
* Pydantic

---

# Setup Instructions

## Step 1: Clone the Repository

```bash
git clone https://github.com/SaakethaSurya/STATIFY_2.0_QuadCore.git
cd STATIFY_2.0_QuadCore
```

---

## Step 2: Create Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

---

## Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Step 4: Configure Environment Variables

Create a `.env` file in the root directory.

Add:

```env
HF_TOKEN=your_huggingface_token_here
```

---

## Step 5: Run the Project

```bash
python Week1.py
```

---

# Example Queries

* "Show Apple stock price"
* "Latest Tesla news"
* "What is the stock price of NVIDIA?"

---

# Repository Structure

```text
STATIFY_2.0_YourTeamName/
│
├── Week1.py
├── tool.py
├── schema.py
├── requirements.txt
├── README.md
├── .env.example
├── .gitignore
```

---

# Notes

* The `.env` file is excluded using `.gitignore`
* Only `.env.example` is uploaded to GitHub
* This project uses open-source Hugging Face models

---


