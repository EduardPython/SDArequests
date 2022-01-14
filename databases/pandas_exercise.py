import pandas as pd

df = pd.read_csv("top100banks.csv")  # add later index_col="bank"

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
