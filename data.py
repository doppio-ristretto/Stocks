import finnhub

key = "bugd5sn48v6s5hg59ba0"
# Setup client
finnhub_client = finnhub.Client(api_key=key)

# Stock candles
res = finnhub_client.stock_candles('AAPL', 'D', 1590988249, 1591852249)
print(res)

#Convert to Pandas Dataframe
import pandas as pd
print(pd.DataFrame(res))
