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

## Week 2: Multi-Agent Financial Analyst & Risk Auditor

### Overview

Week 2 extends the Week 1 Financial Analyst Chatbot into a stateful multi-agent workflow using Retrieval-Augmented Generation (RAG), a local Chroma vector database, SQLite-based persistent memory, and a conditional graph workflow.

The system combines live market data, technical analysis knowledge, and recent news to generate reliable investment recommendations.

---

## Architecture & Workflow

The application consists of three primary agents connected through a state-based workflow.

```text
                    User Query
                         │
                         ▼
                Data Fetcher Agent
                         │
                         ▼
             Technical Analyst Agent
                  (RAG + ChromaDB)
                         │
                         ▼
                 Risk Auditor Agent
                  │               │
        No Contradiction     Contradiction
                  │               │
                  ▼               ▼
          Save to SQLite     Return to
             Memory        Data Fetcher
                  │
                  ▼
             Final Response
```

### 1. Data Fetcher

Responsibilities:

* Accepts a stock ticker from the user.
* Retrieves live stock prices using **yFinance**.
* Calculates technical indicators such as the **14-day RSI**.
* Fetches the latest company-related news using **DuckDuckGo Search**.

---

### 2. Technical Analyst (RAG)

Responsibilities:

* Uses Retrieval-Augmented Generation (RAG).
* Loads technical analysis knowledge from the Zerodha Varsity PDF.
* Splits the document into chunks.
* Generates embeddings using Hugging Face sentence transformers.
* Stores embeddings in a local Chroma vector database.
* Retrieves relevant technical analysis concepts based on live market indicators.
* Produces a preliminary BUY, HOLD, or SELL recommendation.

---

### 3. Risk Auditor

Responsibilities:

* Reviews the preliminary recommendation.
* Compares technical analysis with recent news headlines.
* Detects possible contradictions between technical indicators and breaking news.
* If contradictory information is detected, the workflow loops back to the Data Fetcher for additional analysis.
* Otherwise, the recommendation is approved and returned to the user.

---

## Persistent Memory

The application uses SQLite to maintain persistent chat history.

Stored information includes:

* Timestamp
* User Query
* Stock Ticker
* Current Price
* RSI
* Final Recommendation
* Final Analysis Report

This enables the agent to retain previous conversations and recommendations across multiple executions.

---

## Retrieval-Augmented Generation (RAG)

The knowledge base is created from the Zerodha Varsity Technical Analysis PDF.

Workflow:

1. Load the PDF from the `data/` directory.
2. Split the document into manageable chunks.
3. Generate vector embeddings.
4. Store embeddings inside the local `chroma_db/` directory.
5. Retrieve relevant knowledge whenever technical indicators require interpretation.

---

## Project Structure

```text
STATIFY_2.0_YourTeamName/
│
├── Week1.py
├── tool.py
├── schema.py
│
├── Agent.py
├── tools2.py
├── schema2.py
├── memory.py
│
├── data/
│   └── technical_analysis.pdf
│
├── chroma_db/
│
├── README.md
├── requirements.txt
├── .env.example
└── .gitignore
```

---

## Setup & Execution

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 2. Configure Environment Variables

Create a `.env` file in the project root.

```env
HF_TOKEN=your_huggingface_token
```

---

### 3. Add the Reference PDF

Download the Zerodha Varsity Technical Analysis PDF and place it inside:

```text
data/
```

---

### 4. Generate the Vector Database

The first execution automatically:

* Loads the PDF
* Splits the document
* Generates embeddings
* Creates the local Chroma database

---

### 5. Run the Application

```bash
python Agent.py
```

---

## Technologies Used

* Python
* LangGraph
* LangChain
* ChromaDB
* Hugging Face Transformers
* Sentence Transformers
* yFinance
* DuckDuckGo Search
* SQLite
* Pydantic

---

## Future Improvements

* Support for multiple technical indicators (MACD, Bollinger Bands, Moving Averages).
* More advanced contradiction detection using semantic similarity.
* Multi-user memory management.
* Portfolio-level risk analysis.
* Interactive web interface using Streamlit.

