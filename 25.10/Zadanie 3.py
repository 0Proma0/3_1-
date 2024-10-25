a = input("Podaj pierwsze wyrazenie: ")
b = input("Podaj drugie wyrazenie: ")
def Hammilton(a,b):
    wynik=0
    test = list(zip(a,b))
    for i in range(0,len(a)):
        if(test[i].count(a[i]) != 2):
            wynik+=1
    return wynik
if(len(a)==len(b)):
    print("Wartosc wspolczynnika Hammiltona wynosi: ",Hammilton(a,b))
else:
    print("Wyrazy nie spelniaja zalozenia do obliczenia odleglosci Hammiltona")