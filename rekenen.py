broccoli = 2.98
aubergine = 3.55
witlof = 1.55

aantalBroccoli = 5
aantalAubergine = 7
aantalWitlof = 2

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
