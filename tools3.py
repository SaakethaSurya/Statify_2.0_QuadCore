import numpy as np

def calculate_sma(prices: list, window: int = 20) -> float:
    if len(prices) < window:
        return float(np.mean(prices)) if prices else 0.0
    return float(np.mean(prices[-window:]))

def calculate_ema(prices: list, window: int = 12) -> float:
    if not prices:
        return 0.0
    if len(prices) < window:
        return calculate_sma(prices, window)
    
    alpha = 2 / (window + 1)
    ema = prices[0]
    for price in prices[1:]:
        ema = (price * alpha) + (ema * (1 - alpha))
    return float(ema)

def calculate_macd(prices: list) -> dict:
    if len(prices) < 26:
        return {"macd": 0.0, "signal": 0.0, "histogram": 0.0}
    
    ema_12 = [calculate_ema(prices[:i+1], 12) for i in range(len(prices))]
    ema_26 = [calculate_ema(prices[:i+1], 26) for i in range(len(prices))]
    
    macd_line = [e1 - e2 for e1, e2 in zip(ema_12, ema_26)]
    # Signal line is 9-day EMA of MACD line
    signal_line = calculate_ema(macd_line, 9)
    
    return {
        "macd": float(macd_line[-1]),
        "signal": float(signal_line),
        "histogram": float(macd_line[-1] - signal_line)
    }