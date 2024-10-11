s = "ATGCATATGACTCAATGCCCATTAAAAA"
print("Liczba nukleotydow w sekwencij :",len(s))
print("Liczba wystapien G i C : ",s.count("G")+s.count("C"))
temp = (s.count("G")+s.count("C"))/len(s)*100
print(f"Zawartość procentowa GC w podanej sekwencji to : {temp:.4}%")