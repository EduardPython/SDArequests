import pandas as pd


people = {
    "first": ["Corey", 'Jane', 'John'],
    "last": ["Schafer", 'Doe', 'Doe'],
    "email": ["CoreyMSchafer@gmail.com", 'JaneDoe@email.com', 'JohnDoe@email.com']
}
people_df = pd.DataFrame(people)
print(people_df)
#
# quit()

df = pd.read_csv("top100banks.csv")  # add later index_col="bank"
pd.set_option('display.max_columns', 85)  #must be pd not df
pd.set_option('display.max_rows', 85)
# rank,bank,country,total_assets_us_b,balance_sheet

# PRINT DATAFRAME - all columns
#print(df)
#print(type(df))
#print(df.tail(10))
#print(df.head(15))

# DATAFRAME SHAPE
#print(df.shape)


# ACCESSING COLUMNS AND CELLS
#print(df.columns)
#print(df.bank)
#print(df[["bank","country"]]) # dvojite [[]]
#print(df.loc[0:10, "rank":"country"])
#print(df.iloc[[0,10], [0,1,2]])  #nejde slicing - radek 1-10 musi byt list[0,1,2,3...9]


# SORTING AND INDEXING
#print(df.sort_index(inplace=True)) # --> add index_col, try inplace=False
#print(df)
#print(df.index)
#print(df.set_index("country", inplace=True))# try inplace=False#print(df.index)
#print(df.loc["Japan", ["rank", "bank"]])
#print(df.iloc[4])
#print(df.index)
#df.reset_index(inplace=True)
#print(df.index)¨

# finished with 03 index - continue with filtering - https://github.com/CoreyMSchafer/code_snippets/tree/master/Python/Pandas/04-Filtering

# FILTERING
#filt = (df['bank'] == 'Bank of China') & (df['country'] == 'China') # | == AND
#filt = (df['bank'] == 'Bank of China') #| (df['country'] == 'China') # | == OR
#print(filt)
#print(df.loc[filt, ["total_assets_us_b", "rank"]])  # print all under filter
#print(40*"*")
#print(df.loc[-filt, "total_assets_us_b"]) # printing all NOT in filter


#high_rank = (df["rank"] < 15)
#print(df.loc[high_rank])
#print(df.loc[high_rank,["country", "bank"]])

#eu_countries = ["UK", "France", "Germany", "Italy", "Spain"] # UK not anymore :)
#filt = df["country"].isin(eu_countries)
#print(filt) # bool -> True // False
#print(df.loc[filt]) # 6 7  HSBC Holdings  UK  2,521.77....
#print(df.loc[filt, ["bank"]])  # 6 HSBC Holdings

#filt = df["country"].str.contains('US',na=True) # string that contains "US" (to catch US and USA) and if there is empty value --> it is True
#print(filt)
#filt = df["country"].str.contains('U',na=True)  # UK, USA
#print(df.loc[filt]) # printing only those rows chosen by filter (== containg US)

#df.rename(columns={"bank":"jmeno banky", "country": "zeme"}, inplace=True) #bez inplace to failuje
#print(df["zeme"])
#df["zeme"] = df["zeme"].map({"USA": "Amerika", "China": "Cina"}) # hodi to NAN na všechny ostatni --> lepši použivat s True / False
#print(df["zeme"])
#df["zeme"] = df["zeme"].map({"Cina": True}) # zbytek je NaN
#print(df["zeme"])
#format = lambda x: x.upper()
#df = df["zeme"].map(format) # musíme to dát do proměné --> DF =
#print(df)

# UPDATING DATA
#print(df.loc[0])
#df.loc[0] = [1, "CSOB", "Czechia", "1000", "2020-12-31"]
#print(df.loc[0])
#print(type(df.loc[0, "bank"])) # class str
#print(type(df.loc[0, ["bank", "country"]])) #class <class 'pandas.core.series.Series'>


#print(df.loc[1])
#df.loc[1, ["bank", "country"]] = ["VUB", "Slovakia"]
#print(df.loc[1])

#filt = (df["country"] == "China")
#df.loc[filt, ["country", "bank"]] = ["Cina", "Banka v Cine"]
#print(df)

#print(df["country"].apply(len))

#format = lambda x: x.upper()
#df = df["zeme"].map(format) # musíme to dát do proměné --> DF =
#print(df)

def make_it_upper(name):
    return name.upper()
#df = df["country"].apply(make_it_upper) # nefunfuje bez df = || hodí error s make_it_upper()
#print(df)
#df["country"] = df["country"].apply(lambda x: x.lower())
#print(df)

#print(len(df["rank"]))
#print(len(df["rank", "country"])) # Error - > jen jedna proměná

#print(df.apply(lambda x: x.min())) minima z každého sloupce
#print(df.applymap(len)) # error - int has no len --> same for max, min
#print(people_df.applymap(len))
#print(people_df.applymap(max)) # interesting --> showing highest letter
#print(people_df.applymap(str.lower))

#df['country'] = df['country'].replace({'China': 'Cina', 'USA': 'United States'})
#print(df)



