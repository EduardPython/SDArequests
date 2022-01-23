import pandas as pd

# USE file top100banks.csv

# 1) Seradte banky podle total assets od nejnižší po nejvyšší - Done
# 2) Seradte bank podle abecedy (z-a)
# 3) Vypocitejte soucet všech assets, vypocitejte median vsech assets
# 4) Vytvorte seznam vsech zemi v kterých se banky nachází (a-z)
# 5) Udelejte tabulku - kolik bank je v které zemi (např: USA: 5) (pocet bank - od nejvic do nejmin)
# 6) Udelejte tabulku - kolik bank je v které zemi a kolik mají dohromady assets (a-z)
# 7) Udelejte tabulku kde bude z každé země pouze banky s nejvíce assets (a-z)
# 8) Vypiste banky ktere zacinaji pouze na "B"
# 9) Vypiste banky ktere maji assets nad 1000 mld USD
# 10) Udelejte tabulku - banky zacinajici na stejne pismeno a kolik mají dohromady assets (a-z)

df = pd.read_csv("top100banks.csv")  # add later index_col="bank"
pd.set_option('display.max_columns', 85)  # must be pd not df
pd.set_option('display.max_rows', 85)

# 1
#print(df.loc[::-1]) - reversed order but same indexes
#print(df.loc[::-1].reset_index(drop=True)) # now okay with indexes

# print(type(df.loc[0, "total_assets_us_b"])) # str
# x = float(df.loc[0, "total_assets_us_b"].replace(",","")) # to float
# filt = lambda x: float(x.replace(",", ""))
# df["total_assets_us_b"] = df["total_assets_us_b"].map(filt) # must be df["total_assets_us_b"] = !!!
# print(df)
# print(type(df.loc[0, "total_assets_us_b"]))
# df = df.sort_values(by=["total_assets_us_b"])
# print(df)

# 2
# df = df.sort_values(by=["bank"], ascending=False)
# print(df)

# 3a SUM
# filt = lambda x: float(x.replace(",", ""))
# df["total_assets_us_b"] = df["total_assets_us_b"].map(filt)
# print(df["total_assets_us_b"].sum())

# 3b MED
# print(df["total_assets_us_b"].median())

# 4 Unique countries
# print(df["country"].unique())
# list_of_countries = df["country"].unique() # toto není list --> check with type()
# list_of_countries = list(df["country"].unique()) # toto uz je list
# print(sorted(list_of_countries))
# print(df["country"].nunique())
# print(len(df["country"].unique()))


# 5 kolik bank je v které zemi
# grouped_by_countries = df.groupby("country") #<pandas.core.groupby.generic.DataFrameGroupBy object at 0x102c2c1f0>
# print(grouped_by_countries.first())
# df = df.groupby(by=["country"]).count()
# print(df["bank"])
# print(df["rank"])
# print(df) # sorted by alphabet
# df = df.sort_values(by=["bank"], ascending=False) # sorted by count
# print(df)
# print(df["bank"])


# 6 group by count and sum of assets
#filt = lambda x: float(x.replace(",", ""))
#df["total_assets_us_b"] = df["total_assets_us_b"].map(filt)  #assets to float
#grouped = df.groupby("country").agg({"bank":["count"], "total_assets_us_b": ["sum"]})
#print(grouped)
#print(grouped.sort_values(["country"]))

# 7 Tricky one - get bank from each country with highest amount of assets
# Sort banks by assests

# result = {"countries":[],
#           "assets_amount":[]}
#
# filt_float = lambda x: float(x.replace(",", ""))
# df["total_assets_us_b"] = df["total_assets_us_b"].map(filt_float)
# # Get list of countries
# list_of_countries = list(df["country"].unique()) # musí se to prekonvertovat do listu
# # Iterate thru dataframe -> take coutry -> new_list = mark first bank, coutnry and assets -> pop coutry from list of coutries
# for i in range(len(df)) :
#     country = df.loc[i, "country"]
#     assets = df.loc[i,"total_assets_us_b"]
#     if country in list_of_countries:
#         result["countries"].append(country)
#         result["assets_amount"].append(assets)
#         list_of_countries.remove(country)
#
# result_df = pd.DataFrame(result)
# print(result_df)

# make dataframe from new_list

# 8 Banks starts with "B"
# filt = df["bank"].str.startswith('B')  # UK, USA
# print(df.loc[filt])

# 9 banky na 1000 asests
# filt_float = lambda x: float(x.replace(",", ""))
# df["total_assets_us_b"] = df["total_assets_us_b"].map(filt_float)
#
# filt_assets = df[df["total_assets_us_b"]> 1000]
# print(filt_assets)

# 10 Udelejte tabulku - banky zacinajici na stejne pismeno a kolik mají dohromady assets (a-z)
# přidat nový sloupec s prvním písmenem
# pokračovat jak v cvičení 6
# df["first_letter"] = df["bank"].astype(str).str[0]
# print(df["first_letter"])
# print(df)
# filt = lambda x: float(x.replace(",", ""))
# df["total_assets_us_b"] = df["total_assets_us_b"].map(filt)  #assets to float
# grouped = df.groupby("first_letter").agg({"bank":["count"], "total_assets_us_b": ["sum"]})
# print(grouped)




