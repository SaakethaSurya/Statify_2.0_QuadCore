from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings

loader = PyPDFLoader("data/technical_analysis.pdf")

documents = loader.load()

splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)

docs = splitter.split_documents(documents)

embedding = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

db = Chroma.from_documents(
    docs,
    embedding,
    persist_directory="chroma_db"
)

retriever = db.as_retriever()

def technical_analyst(rsi):

    if rsi > 70:
        query = "RSI above 70"

    elif rsi < 30:
        query = "RSI below 30"

    else:
        query = "neutral RSI"

    results = retriever.invoke(query)

    context = results[0].page_content

    if rsi > 70:
        recommendation = "SELL"

    elif rsi < 30:
        recommendation = "BUY"

    else:
        recommendation = "HOLD"

    return recommendation, context

def risk_auditor(recommendation, news):

    bullish_words = [
        "contract",
        "growth",
        "profit",
        "acquisition",
        "surge"
    ]

    contradiction = False

    if recommendation == "SELL":

        for headline in news:

            for word in bullish_words:

                if word.lower() in headline.lower():
                    contradiction = True

    return contradiction

from tools2 import fetch_stock_data, fetch_news

ticker = input("Enter ticker: ")

data = fetch_stock_data(ticker)

news = fetch_news(ticker)

recommendation, context = technical_analyst(data["rsi"])

contradiction = risk_auditor(
    recommendation,
    news
)

print("\n--- ANALYSIS ---")
print("Price:", data["price"])
print("RSI:", data["rsi"])
print("Recommendation:", recommendation)

print("\nRAG Context:")
print(context)

print("\nNews:")
for n in news:
    print("-", n)

if contradiction:
    print("\nRisk Auditor Warning:")
    print("Contradictory bullish news detected.")
    print("Re-running deeper analysis...")
else:
    print("\nRisk Auditor Approved.")