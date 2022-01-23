import pandas as pd

countries = {
'country': ['United States', 'The Netherlands', 'Spain', 'Mexico', 'Australia'],
'capital': ['Washington D.C.', 'Amsterdam', 'Madrid', 'Mexico City', 'Canberra'],
'continent': ['North America', 'Europe', 'Europe', 'North America', 'Australia'],
'language': ['English', 'Dutch', 'Spanish', 'Spanish', 'English']}

countries_df = pd.DataFrame(countries)
countries_df = countries_df.set_index("country")
#print(countries_df)

# 3) hlavní město Mexika
#print(countries_df.loc["Mexico", "capital"])
#print(countries_df.iloc[3, 0])

# 4) získat všechny jazyky
#print(countries_df.loc[:,'language'])
#print(countries_df.iloc[:,2])

# 5) všechny data pro Španělsko
print(countries_df.loc["Spain", :])
print(40*"*")
print(countries_df.iloc[2, :])

