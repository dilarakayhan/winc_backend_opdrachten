# price per vegetable
broccoli = 2.98  # assigning broccoli a value of 2.98
aubergine = 3.55  # assigning aubergine a value of 3.55
witlof = 1.55  # assigning witlof a value of 1.55

# amount per vegetables
aantalBroccoli = 5
aantalAubergine = 7
aantalWitlof = 2

"""
~~ Calculation of Les Légumes ~~
"""

bedragGroenten = broccoli + aubergine + witlof
gemiddeldeGroentenPrijs = bedragGroenten / 3
aantalGroenten = aantalBroccoli + aantalAubergine + aantalWitlof
totaalBedragGroenten = bedragGroenten * aantalGroenten
kortingPercentage = bedragGroenten * aantalGroenten / 100 * 15
totaalPrijsMinKorting = totaalBedragGroenten - kortingPercentage

print("Prijs groenten: ", round(bedragGroenten, 2))
print("Gemiddelde prijs groenten: ", round(gemiddeldeGroentenPrijs, 2))
print("Totaal aantal groenten: ", aantalGroenten)
print("Bedrag aantal groenten keer prijs: ", totaalBedragGroenten)
print("Korting: ", round(kortingPercentage, 2))
print("Totaal min korting: ", round(totaalPrijsMinKorting, 2))
