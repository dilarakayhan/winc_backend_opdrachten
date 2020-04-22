# players
hans = "Hans van Breukelen"
berry = "Berry van Aerle"
frank = "Frank Rijkaard"
ronald = "Ronald Koeman"
adri = "Adri van Tiggelen"
gerald = "Gerald Vanenburg"
arnold = "Arnold Mühren"
jan = "Jan Wouters"
erwin = "Erwin Koeman"
marco = "Marco van Basten"
ruud = "Ruud Gullit"

# subs
joop = "Joop Hiele"
wilber = "Wilbert Suvrijn"
johnS = "John van 't Schip"
johnB = "John Bosman"
wim = "Wim Kieft"

# players who've scored
playersWhoScored = ruud + " " + marco

# minutes in which the goals have been scored
goalOne = 35
goalTwo = 54

# last name first
hans_lastname_first = hans[hans.find(" ")+1:] + ", " + hans[0:hans.find(" ")]

# initial with last name
hans_initial = hans[0:1] + ". " + hans[hans.find(" ")+1:]

# name times 4 (literally)
hans_four_times = (len(hans[0:hans.find(" ")]) *
                   (hans[0:hans.find(" ")] + "! "))


print(f"{ruud} scoorde de eerste goal in minuut {goalOne}\n{marco} scoorde de tweede goal in minuut {goalTwo}")
print(playersWhoScored)
print(hans_lastname_first)
print(hans_initial)
print(hans_four_times)

# whether last character is a space true or false
print(hans_four_times[-1] == " ")
