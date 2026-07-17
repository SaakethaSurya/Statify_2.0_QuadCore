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

# Week 3: Containerized MCP-Powered Multi-Agent Deployment

## Overview

Week 3 transforms **Statify 2.0** from a standalone multi-agent application into a production-oriented microservice architecture.

The application is decomposed into independent services communicating through the **Model Context Protocol (MCP)**. The AI orchestration layer, quantitative analytics engine, and API gateway operate as separate components deployed inside Docker containers, allowing each service to scale, update, and execute independently.

This architecture follows modern AI deployment practices by separating business logic from analytical computation while exposing the entire workflow through a RESTful FastAPI interface.

---

# System Architecture

```text
                            Client

                              │
                     HTTP POST Request

                              │
                              ▼

                     FastAPI Gateway (API)

                              │
                              ▼

                   LangGraph Multi-Agent System

                              │
                              ▼

                    MultiServerMCPClient

                              │
               Docker Internal Bridge Network
                              │
                              ▼

                  MCP Quantitative Server

                    ├── Trading Theory
                    ├── Market Indicators
                    ├── Technical Analysis
                    └── Mathematical Models

                              │
                              ▼

                     JSON Response Returned
```

---

# Service Overview

## 1. FastAPI Gateway (`main.py`)

The FastAPI application serves as the public entry point of the platform.

### Responsibilities

* Exposes REST API endpoints
* Validates incoming requests using Pydantic
* Initializes the MCP client during application startup
* Executes the LangGraph workflow
* Returns structured JSON responses
* Performs graceful shutdown of active resources

The application utilizes FastAPI's **lifespan context manager** to ensure that long-lived MCP connections are created only once during startup and are closed cleanly when the application terminates.

---

## 2. MCP Client (`mcp_client.py`)

The MCP client acts as the communication bridge between the LangGraph workflow and remote analytical services.

### Responsibilities

* Creates and maintains MCP client sessions
* Connects to the MCP server over Docker's internal network
* Discovers remote analytical tools
* Invokes tools asynchronously
* Handles communication failures gracefully
* Returns structured error information to the agent workflow

Rather than allowing network or execution failures to terminate the application, the client captures exceptions and propagates structured error responses back to the orchestration layer, enabling the agent to recover or retry execution.

---

## 3. MCP Server (`mcp_server.py`)

The MCP server hosts the quantitative analysis engine.

It exposes analytical capabilities as remote MCP tools that can be consumed by any compatible MCP client.

### Registered Capabilities

* Technical Analysis Retrieval
* Market Indicator Analysis
* Trading Knowledge Retrieval
* Mathematical Calculations

The server is implemented using the asynchronous MCP framework and exposed through a lightweight Starlette application running inside its own Docker container.

---

## 4. Quantitative Analysis Engine (`tools3.py`)

This module contains the mathematical foundation of the application.

Unlike previous weeks, no AI-specific logic exists here.

The module focuses solely on deterministic financial computations.

Implemented indicators include:

* Simple Moving Average (SMA)
* Exponential Moving Average (EMA)
* Moving Average Convergence Divergence (MACD)
* Signal Line
* MACD Histogram

Keeping analytical logic independent of networking and AI frameworks improves maintainability, testing, and future extensibility.

---

## 5. Data Validation Layer (`schema3.py`)

Pydantic v2 models define the contract between the client and server.

Responsibilities include:

* Request validation
* Response serialization
* Type enforcement
* Automatic API documentation generation
* Input constraint verification

This ensures that malformed requests are rejected before entering the analytical pipeline.

---

# Docker Deployment

The project is deployed using Docker Compose.

Containerization provides:

* Service isolation
* Reproducible deployments
* Independent scaling
* Simplified dependency management
* Portable execution across environments

The deployment consists of two primary services:

### API Service

Responsible for:

* FastAPI
* LangGraph orchestration
* MCP Client
* Request processing

### Vector Service

Responsible for:

* MCP Server
* Quantitative calculations
* Technical analysis retrieval
* Financial computation tools

Both services communicate exclusively through Docker's internal bridge network.

---

# MCP Communication Flow

Unlike Week 2, where all analytical components executed within the same process, Week 3 introduces protocol-based communication.

Workflow:

1. The client submits an analysis request to the FastAPI endpoint.
2. FastAPI validates the payload.
3. The LangGraph workflow determines which analytical capability is required.
4. The MCP Client invokes the corresponding remote MCP tool.
5. The MCP Server executes the requested computation.
6. Results are streamed back to the client over the MCP transport.
7. The LangGraph workflow integrates the returned context.
8. A structured investment report is generated and returned to the client.

This design decouples orchestration from computation, allowing analytical services to evolve independently of the AI workflow.

---

# Fault-Tolerant Execution

Reliability is a key objective of the Week 3 architecture.

If an MCP communication error or remote tool failure occurs:

* the exception is captured,
* a structured error is propagated back to the workflow,
* the application remains operational,
* and the agent can decide whether to retry, request alternative information, or return a meaningful failure response.

This approach prevents individual service failures from terminating the overall system.

---

# Technology Stack

* Python 3.12
* FastAPI
* LangGraph
* LangChain
* Model Context Protocol (MCP)
* langchain-mcp-adapters
* Starlette
* Docker
* Docker Compose
* Pydantic v2
* Uvicorn

---

# Architectural Improvements from Week 2

| Week 2                          | Week 3                                            |
| ------------------------------- | ------------------------------------------------- |
| Monolithic multi-agent workflow | Distributed microservice architecture             |
| Local analytical execution      | Remote MCP-powered analytical services            |
| Direct module invocation        | Protocol-driven tool discovery and execution      |
| Single-process execution        | Multi-container deployment                        |
| Local orchestration             | Containerized API gateway with remote computation |
| Basic deployment                | Production-oriented Docker environment            |

---

# Conclusion

Week 3 completes the transition of **Statify 2.0** from a prototype conversational financial assistant into a modular, service-oriented AI platform.

By introducing Docker, FastAPI, MCP-based communication, and distributed analytical services, the application now reflects many of the architectural principles used in modern production AI systems, including loose coupling, protocol-driven interoperability, scalability, and fault tolerance.
