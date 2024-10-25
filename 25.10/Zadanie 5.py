import math
def pierwiasek(x):
    
    return "{:.3f}".format(math.sqrt(x))
lista_skladana = [pierwiasek(i) for i in range(0,20) if i%2!=0]
map_filter = list(map(pierwiasek,filter(lambda y : y%2!=0,range(0,20))))

print("Sposob z uzyciem listy skladanej: ",", ".join(lista_skladana))
print("Sposob z uzyciem map i filter: ",", ".join(map_filter))