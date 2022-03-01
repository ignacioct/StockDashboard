# Stock Portfolio Dashboard Dashboard
Personal Stock Dashboards made using Python and Streamlit

## Installing Dependencies

Streamlit is mainly powered by Streamlit and Seaborn. There's a requirement text file from where a Conda environment can be easily built.

```bash
conda env create -n stock_dashboard -f environment.txt python=3.7
conda activate stock_dashboard
pip install yahoo_fin
pip install streamlit
```

## Uploading your portfolio data

The app will search for a file called ```portfolio.csv``` in your parent directory. There, a table information about your portfolio should be placed. This csv file has the following variables to fill up: Stock Symbol, Price (at which it was bought), Money Invested, Date of purcharse. 

## Running the Dashboard

To run the app, once the environment is activated, just type the following Streamlit command:

```bash
streamlit run app.y
```

