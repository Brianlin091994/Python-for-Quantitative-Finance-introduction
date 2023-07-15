import math

def find_indicators(prices: list, **kwargs):
    
    if "ma" in kwargs:
        window = kwargs["ma"]
        ma = sum(prices[-window:]) / window
        print(f"Moving Average ({window}) is {ma}")

    if "volatility" in kwargs:
        window = kwargs['volatility']
        mean = sum(prices) / len(prices)
        squared_diff_sum = sum((price - mean) ** 2 for price in prices)
        mean_squared_diff = squared_diff_sum / len(prices)
        volatility = math.sqrt(mean_squared_diff)
        print(f"Volatility of {window} is {volatility}")
    
