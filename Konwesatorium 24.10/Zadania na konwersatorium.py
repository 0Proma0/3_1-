abstrakt = "Phospholipid membranes support essential biochemical processes, yet remain difficult to characterize due to their compositional and structural heterogeneity. The two most common phospholipid headgroup structures in biological membranes are phosphatidylcholine (PC) and phosphatidylethanolamine (PE), but interactions between PC and PE lipids remain underexplored. In this study, we apply ultrafast two-dimensional infrared (2D IR) spectroscopy to quantify the headgroup effects on interfacial dynamics in PC/PE lipid mixtures. Experiments are interpreted through molecular dynamics simulations using the molecular dynamics with alchemical step (MDAS) algorithm for enhanced sampling. Experimental results indicate that the PE content decreases H-bond formation at the ester carbonyl positions near the lipid membrane's hydrophobic core as a result of increased packing density. The observed dehydration is linked to faster molecular dynamics within the interfacial region."

def LiczText(abstrakt):
    LiczbaZdan = abstrakt.count(".")
    print("Liczba zdan wynosi: ",LiczbaZdan)
    LiczbaSlow = abstrakt.replace(',',' ')
    LiczbaSlow = LiczbaSlow.replace('.',' ').split()
    print("Liczba slow wynosi: ",len(LiczbaSlow))
    NajdluzszeSlowo = max(LiczbaSlow,key=len)
    print("Najdluzsze slowo: ",NajdluzszeSlowo)
    DluzejNiz5 = [slowo for slowo in LiczbaSlow if len(slowo)>5]
    NajczeszczeSlowo = max(set(DluzejNiz5), key=(DluzejNiz5.count))
    print("Najczeszcze slowo: ",NajczeszczeSlowo)

def FormatZnak(abstrakt, dlug):
    slowa = abstrakt.split()
    linie = []
    obecna_linia = []
    for word in slowa:
        if len(' '.join(obecna_linia + [word])) > dlug:
            linie.append(' '.join(obecna_linia))
            obecna_linia = [word]
        else:
            obecna_linia.append(word) 
    if obecna_linia:
        linie.append(' '.join(obecna_linia))
    for line in linie:
        print(line.rjust(dlug))


def OdwrSlowo(abstrakt):
    slowa = abstrakt.split()
    SlowReverse = [slowo[::-1] for slowo in slowa]
    return ' '.join(SlowReverse)

def DlugSlowWZdaniu(abstrakt):
    zdania = abstrakt.split(sep=".")
    for zdanie in zdania:
        if not zdanie.strip():
            continue
        slowa = zdanie.split()
        SlowoDlug = [len(slowo) for slowo in slowa]
        print(f"Zdanie: {zdanie}")
        print("Dlugosci slow: ",SlowoDlug)
        if len(SlowoDlug) > 0:
            SredDlug = sum(SlowoDlug) / len(SlowoDlug)
        else:
            SredDlug = 0
        print(f"Srednia dlugosc slowa: {SredDlug:.2f}")
        print("*"*50)
