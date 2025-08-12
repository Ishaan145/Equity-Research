def calculate_macd(data, short_window=12, long_window=26, signal_window=9):
    short_ema = data['Adj Close'].ewm(span=short_window, adjust=False).mean()
    long_ema = data['Adj Close'].ewm(span=long_window, adjust=False).mean()
    macd_line = short_ema - long_ema
    signal_line = macd_line.ewm(span=signal_window, adjust=False).mean()
    histogram = macd_line - signal_line
    return macd_line, signal_line, histogram

bse_history_data, bse_history_data, bse_history_data = calculate_macd(bse_history_data)

print("\nLast 5 MACD values for BSE:")
print(bse_history_data].tail())
