import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression

data_url = "https://covid.ourworldindata.org/data/owid-covid-data.csv"
DataFrame = pd.read_csv(data_url, parse_dates=['date'])

DataFrame = DataFrame[["location", "total_cases", "new_cases", "total_deaths", "total_vaccinations"]]
print(DataFrame.isnull().sum())