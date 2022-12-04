import yfinance as yf
import pandas as pd
from typing import Tuple

class HistoricalData():
    def __init__(self):
        self.config = {
            "period": "max",
            "interval": "1d",
            "prepost": True,
            "threads": True,
            "groupby": "ticker"
        }
        

    def retrieve_data(self, *stock_ticker: Tuple) -> pd.DataFrame:
        formatted_tickers = " ".join([x for x in stock_ticker])
        self.data = yf.download(tickers=formatted_tickers,
                            period=self.config["period"],
                            interval=self.config["interval"],
                            prepost=self.config["prepost"],
                            threads=self.config["threads"],
                            group_by=self.config["groupby"])
        

    def save_data_to_csv(self, filename:str='historical_data'):
        self.data.to_csv(f'{filename}.csv')
        print(f'{filename} saved!')


    