names_list = ("Dill Doe", "Chris P. Bacon", "Ben Dover")
update = "Harry Dixon"
names_updated = list(names_list)
names_updated.append(update)
input = input("Podaję imię : ")
b = input in names_updated
print(b)