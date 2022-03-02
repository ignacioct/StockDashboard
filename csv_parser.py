"""
Class in charge of parsing the contents of the CSV file.
The data is saved on a Pandas Dataframe.
"""

import pandas as pd
from yahoo_fin import stock_info as si

class Portfolio:

    def __init__(self, path) -> None:
        
        self.csvPath = path

        # Load basic DF
        self.df = pd.read_csv(self.csvPath)

        # Adding extra columns
        moneyInvestedList = []
        currentPriceList = []
        currentValueInvestmentList = []
        gainLossList = []
        positiveList = []
        
        for _, row in self.df.iterrows():
            
            # Obtaining extra variables
            moneyInvested = row["Price"]*row["Amount"]
            currentPrice = si.get_live_price(row["Stock"].lower())
            gainLoss = (currentPrice - row["Price"]) *100 / row["Price"]
            currentValueInvestment = (currentPrice*row["Amount"]) - (row["Price"]*row["Amount"])
            positive = True if gainLoss > 0 else False

            # Adding them to lists
            moneyInvestedList.append(moneyInvested)
            currentPriceList.append(currentPrice)
            currentValueInvestmentList.append(currentValueInvestment)
            positiveList.append(positive)
            gainLossList.append(gainLoss)

        # Adding new lists as columns of the DataFrame
        self.df["Money Invested"] = moneyInvestedList
        self.df["Current Price"] = currentPriceList
        self.df["Gain/Loss %"] = gainLossList
        self.df["Current Value Investment"] = currentValueInvestmentList
        
        # Rounding floats to two decimals digits
        self.df = self.df.round(2)