prei_prijs = str(2)
prei_bestelling = "prei 4"
prei_bestelling_int = prei_bestelling[prei_bestelling.find(" ")+1]

broccoli_prijs = 2.34
broccoli_bestelling = "broccoli 1.6"
broccoli_bestelling_find = broccoli_bestelling[broccoli_bestelling.find(
    " ")+1:]
broccoli_bestelling_find_int = float(broccoli_bestelling_find)
broccoli_totaalprijs = broccoli_prijs * broccoli_bestelling_find_int

print(f"Prei kost {prei_prijs} euro per kilo")
print(int(prei_bestelling_int))
print(f"{broccoli_bestelling_find} kilo broccoli kost {round(broccoli_totaalprijs, 2)} euro")
