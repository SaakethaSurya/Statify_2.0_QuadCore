import yfinance as yf
from duckduckgo_search import DDGS


def fetch_stock_data(ticker):
    stock = yf.Ticker(ticker)
    hist = stock.history(period="1mo")

    close_prices = hist["Close"]

    latest_price = close_prices.iloc[-1]

    delta = close_prices.diff()

    gain = delta.where(delta > 0, 0).rolling(14).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(14).mean()

    rs = gain / loss

    rsi = 100 - (100 / (1 + rs))

    latest_rsi = rsi.iloc[-1]

    return {
        "price": float(latest_price),
        "rsi": float(latest_rsi)
    }


def fetch_news(company):
    headlines = []

    with DDGS() as ddgs:
        results = ddgs.text(
            f"{company} stock market news",
            max_results=5
        )

        for r in results:
            headlines.append(r["title"])

    return headlines