import pandas as pd


countries_df = pd.DataFrame({
'country': ['United States', 'The Netherlands', 'Spain', 'Mexico', 'Australia'],
'capital': ['Washington D.C.', 'Amsterdam', 'Madrid', 'Mexico City', 'Canberra'],
'continent': ['North America', 'Europe', 'Europe', 'North America', 'Australia'],
'language': ['English', 'Dutch', 'Spanish', 'Spanish', 'English']})

countries_df = countries_df.set_index("country")
#print(countries_df)

#print(countries_df.loc["Mexico", "capital"])
#print(countries_df.iloc[3,0])
#print(countries_df.iloc[[3],[0]])

#print(countries_df.loc[:, "language"])
#print(countries_df.iloc[:,2])
# k zamyšlení
#print(countries_df.loc["Spain", :])
