"""
Class in charge of parsing the contents of the CSV file.
The data is saved on a Pandas Dataframe.
"""
import datetime

import pandas as pd
from yahoo_fin import stock_info as si


class Portfolio:
    def __init__(self, path) -> None:

        self.csvPath = path

        # Load basic DF
        df = pd.read_csv(self.csvPath)

        # Adding extra columns
        currentPriceList = []
        currentValueInvestmentList = []
        gainLossList = []
        positiveList = []

        # Aggregate stocks of the same type
        aggregation_functions = {"Price": "mean", "Money Invested": "sum"}
        df = df.groupby(["Stock"], as_index=False).aggregate(aggregation_functions)

        self.df = df

        for _, row in self.df.iterrows():

            # Obtaining extra variables
            currentPrice = si.get_live_price(row["Stock"].lower())
            gainLoss = (currentPrice - row["Price"]) * 100 / row["Price"]
            numberOfStocks = row["Money Invested"] / row["Price"]
            currentValueInvestment = (currentPrice * numberOfStocks) - (
                row["Money Invested"]
            )
            positive = True if gainLoss > 0 else False

            # Adding them to lists
            currentPriceList.append(currentPrice)
            currentValueInvestmentList.append(currentValueInvestment)
            positiveList.append(positive)
            gainLossList.append(gainLoss)

        # Adding new lists as columns of the DataFrame
        self.df["Current Price"] = currentPriceList
        self.df["Gain/Loss %"] = gainLossList
        self.df["Current Value Investment"] = currentValueInvestmentList

        # Rounding floats to two decimals digits
        self.df = self.df.round(2)

        # Obtaining the total money invested
        self.totalMoneyInvested = self.df["Money Invested"].sum()
