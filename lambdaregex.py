

zvirata =["otter", "whale", "goose", "chipmunk", "fox", "sheep", "rabbit", "marten"]
sorted_zvirata = sorted(zvirata, key=lambda x: len(x))

mesta_populace =[(19542209, "New York") ,(4887871, "Alabama"), (1420491, "Hawaii"), (626299, "Vermont"), (1805832, "West Virginia"), (39865590, "California")]
max_populace = sorted(mesta_populace, key=lambda x: x[0], reverse=True)
mesta_podle_abecedy = sorted(mesta_populace, key=lambda x: x[1])

programmer = [{'Name':'Mark', 'Programming':'Python', 'Year of Experience': 3},
               {'Name':'Nicole', 'Programming':'C', 'Year of Experience': 1},
               {'Name':'Jason', 'Programming':'R', 'Year of Experience': 10}]

sorted_programmer = sorted(programmer, key=lambda x: x['Year of Experience'], reverse=True)

cisla = [44,54,64,74,104]
plus_sest = [i+6 for i in cisla]

cars_kilos ={"Sedan": 1500, "SUV": 2000, "Pickup": 2500, "Minivan": 1600, "Van": 2400, "Semi": 13600, "Bicycle": 7, "Motorcycle": 110}

car_names_up_to_2500 = [car for car in cars_kilos if cars_kilos[car]<2500]


akcie = ["META", "GOOG", "AMZN", "NTFX", "AAPL"]
cena = [100, 130, 160, 299, 120]
akcie_cena = zip(akcie, cena)
print(list(akcie_cena))
akcie_cena = {stock:price for stock,price in zip(akcie, cena)}