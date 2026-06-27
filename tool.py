import yfinance as yf
from duckduckgo_search import DDGS

def get_stock_price(company: str):
    stock = yf.Ticker(company)
    data = stock.history(period="1d")

    if data.empty:
        return "No stock data found."

    latest_price = data["Close"].iloc[-1]

    return f"Latest stock price of {company}: ${latest_price:.2f}"


def get_company_news(company: str):
    results = []

    with DDGS() as ddgs:
        news = ddgs.text(f"{company} latest stock market news", max_results=5)

        for item in news:
            results.append(item["title"])

    return "\n".join(results)