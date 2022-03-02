"""
Stock Dashboard App. 

Visualization of portfolios. Made with Python 3.7 and Streamlit.
Ignacio Talavera Cepeda, 2022.
"""

from csv_parser import Portfolio

import matplotlib.pyplot as plt
import matplotlib
import pandas as pd
import seaborn as sns
import streamlit as st

matplotlib.rcParams["axes.grid"] = True
matplotlib.rcParams["savefig.transparent"] = True


def donughtDiversity(portfolio: pd.DataFrame) -> None:
    """
    Creating a donught chart with the diversity of the Portfolio.

    Args:
        portfolio: Pandas dataframe with the contents of the csv and some postprocessing data.
    """

    # Define Seaborn color palette to use
    # When there are more than 5 stocks, this might go a little crazy
    colors = sns.color_palette("pastel")[0:5]

    # Define Data and labels
    data = []
    labels = []

    for _, row in portfolio.iterrows():
        data.append(row["Amount"])
        labels.append(row["Stock"])

    # Pie chart in which the donught chart is based
    plt.pie(data, labels=labels, colors=colors, autopct="%.0f%%")

    # add a circle at the center to transform it in a donut chart
    my_circle = plt.Circle((0, 0), 0.7, color="white")
    p = plt.gcf()
    p.gca().add_artist(my_circle)


def main() -> None:

    st.set_page_config(layout="wide")

    # Load the portfolio
    portfolio = Portfolio("portfolio.csv")

    # Header

    st.markdown(
        "<h1 style='text-align: center;'>Stock Portfolio Dashboard</h1>",
        unsafe_allow_html=True,
    )
    st.markdown(
        "<h4 style='text-align: center;'>A Web App by <a href=https://github.com/ignacioct>Ignacio Talavera</a></h4>",
        unsafe_allow_html=True,
    )

    # State of Portfolio and Diversity share row
    firstCol, _, secondCol = st.columns((2.5, 0.75, 1.5))

    # Show dataframe of own stocks
    firstCol.header("Current State of Portfolio")

    # We need to pass the styler to pandas to show only 2 decimals digits.
    firstCol.dataframe(
        portfolio.df.style.format(
            {
                "Price": "{:.2f}",
                "Money Invested": "{:.2f}",
                "Gain/Loss %": "{:.2f}",
                "Current Price": "{:.2f}",
                "Current Value Investment": "{:.2f}",
            }
        )
    )

    # Show pie chart with portfolio diversity
    secondCol.header("Portfolio Diversity")

    fig = plt.figure()
    donughtDiversity(portfolio.df)
    secondCol.pyplot(fig)


if __name__ == "__main__":
    main()
