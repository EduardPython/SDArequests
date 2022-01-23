import pandas as pd

# Zpracovat data od Data acquisition týmu a poskytnout odpovědi na otázky:
df = pd.read_csv('crash_data_honza.csv')

# 1) kolik zemřelo celkem v historii lidí v dopravních nehodách
pocet_mrtvych = (df['no_deaths'].sum())
print(f"V historii létání v dopravních nehodách zemřelo {pocet_mrtvych} lidí")
print(40*'*')

# 2) kolik lidí přežilo pád letadla
pocet_prezivsich = (df['no_survivors'].sum())
print(f"V historii létání přežilo dopravní nehody {pocet_prezivsich} lidí")
print(40*'*')

# 3) jaký byl nejtragičtější rok a dekáda v letectví (dekáda 1920-1929, 1930-1939...2010-2019)

years = []
counter = 0
data_no_deaths_per_year = {}
for i in range(len(df)):
    year = int(df.loc[i, "date"][-4:])
    p_mrtvych = int(df.loc[i, "no_deaths"])
    if year not in years:
        years.append(year)
        counter = 0
    else:
        counter += p_mrtvych
    data_no_deaths_per_year[year] = counter

max_death = max(data_no_deaths_per_year.items(), key=lambda x : x[1])
print(f"Nejvíce lidí zahynulo v letectví v roce {max_death[0]}, bylo jich {max_death[1]}")


decades = []
counter = 0
data_no_deaths_per_decade = {}
for i in range(len(df)):
    decade = int(df.loc[i, "date"][-4:-1])
    p_mrtvych = int(df.loc[i, "no_deaths"])
    if decade not in decades:
        decades.append(decade)
        counter = 0
    else:
        counter += p_mrtvych
    data_no_deaths_per_decade[decade] = counter

max_death_decade = max(data_no_deaths_per_decade.items(), key=lambda x : x[1])
print(f"Nejvíce lidí zahynulo v letectví v dekádě {max_death_decade[0]}0, bylo jich {max_death_decade[1]}")


# 4) který rok a dekádu přežilo nejvíce lidí pády letadla
years = []
counter = 0
data_no_survivors_per_year = {}
for i in range(len(df)):
    year = int(df.loc[i, "date"][-4:])
    p_mrtvych = int(df.loc[i, "no_survivors"])
    if year not in years:
        years.append(year)
        counter = 0
    else:
        counter += p_mrtvych
    data_no_survivors_per_year[year] = counter

max_survivors = max(data_no_survivors_per_year.items(), key=lambda x : x[1])
print(f"Nejvíce lidí přežilo pád letadla v roce {max_survivors[0]}, bylo jich {max_survivors[1]}")


decades = []
counter = 0
data_no_survivors_per_decade = {}
for i in range(len(df)):
    decade = int(df.loc[i, "date"][-4:-1])
    p_mrtvych = int(df.loc[i, "no_survivors"])
    if decade not in decades:
        decades.append(decade)
        counter = 0
    else:
        counter += p_mrtvych
    data_no_survivors_per_decade[decade] = counter

max_survivors_dec = max(data_no_survivors_per_decade.items(), key=lambda x : x[1])
print(f"Nejvíce lidí přežilo pády v letectví v dekádě {max_survivors_dec[0]}0, bylo jich {max_survivors_dec[1]}")


#5) udělat přehled v jakých státech spadly letadla a kolik měly obětí - vypsat top 20
df_5 = df.groupby('state')['no_deaths'].sum().nlargest(20)
print("Top 20 zemí leteckých neštěstí a počet mrtvých")
print(df_5)
print(40*'*')

# 6) udělat přehled kolik lidí zahynulo v pádech podle výrobce letadla
print("Top 20 výrobců letadel a počet mrtvých")
df_6 = df.groupby('aircraft_brand')['no_deaths'].sum().nlargest(20)
print(df_6)