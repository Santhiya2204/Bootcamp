# Databricks notebook source
data = {
    "Year": [2000, 2005, 2010, 2015, 2020],
    "Total Cell Phones": [500000000, 2000000000, 4500000000, 7000000000, 8500000000],
    "Population": [6000000000, 6500000000, 7000000000, 7500000000, 7800000000],
}
df = pd.DataFrame(data)
df["Cell Phones per Person"] = df["Total Cell Phones"] / df["Population"]
plt.figure(figsize=(10, 5))
plt.plot(df["Year"], df["Total Cell Phones"], marker='o', label="Total Cell Phones", color='blue')
plt.plot(df["Year"], df["Cell Phones per Person"], marker='s', label="Cell Phones per Person", color='red')
plt.xlabel("Year")
plt.ylabel("Count")
plt.title("Rise of Cell Phones & Cell Phones Per Person Over Time")
plt.legend()
plt.grid(True)
plt.show()


# COMMAND ----------

pip install pandas

# COMMAND ----------


import pandas as pd


data = {
    "Year": [2000, 2005, 2010, 2015, 2020],
    "Total Cell Phones": [500000000, 2000000000, 4500000000, 7000000000, 8500000000],
    "Population": [6000000000, 6500000000, 7000000000, 7500000000, 7800000000],
}
df = pd.DataFrame(data)
df["Cell Phones per Person"] = df["Total Cell Phones"] / df["Population"]
plt.figure(figsize=(10, 5))
plt.plot(df["Year"], df["Total Cell Phones"], marker='o', label="Total Cell Phones", color='blue')
plt.plot(df["Year"], df["Cell Phones per Person"], marker='s', label="Cell Phones per Person", color='red')
plt.xlabel("Year")
plt.ylabel("Count")
plt.title("Rise of Cell Phones & Cell Phones Per Person Over Time")
plt.legend()
plt.grid(True)
plt.show()


# COMMAND ----------

pip install matplotlib


# COMMAND ----------


import pandas as pd
import matplotlib.pyplot as plt


data = {
    "Year": [2000, 2005, 2010, 2015, 2020],
    "Total Cell Phones": [500000000, 2000000000, 4500000000, 7000000000, 8500000000],
    "Population": [6000000000, 6500000000, 7000000000, 7500000000, 7800000000],
}
df = pd.DataFrame(data)
df["Cell Phones per Person"] = df["Total Cell Phones"] / df["Population"]
plt.figure(figsize=(10, 5))
plt.plot(df["Year"], df["Total Cell Phones"], marker='o', label="Total Cell Phones", color='blue')
plt.plot(df["Year"], df["Cell Phones per Person"], marker='s', label="Cell Phones per Person", color='red')
plt.xlabel("Year")
plt.ylabel("Count")
plt.title("Rise of Cell Phones & Cell Phones Per Person Over Time")
plt.legend()
plt.grid(True)
plt.show()

