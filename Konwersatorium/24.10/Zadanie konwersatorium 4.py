abstrakt = "Phospholipid membranes support essential biochemical processes, yet remain difficult to characterize due to their compositional and structural heterogeneity. The two most common phospholipid headgroup structures in biological membranes are phosphatidylcholine (PC) and phosphatidylethanolamine (PE), but interactions between PC and PE lipids remain underexplored. In this study, we apply ultrafast two-dimensional infrared (2D IR) spectroscopy to quantify the headgroup effects on interfacial dynamics in PC/PE lipid mixtures. Experiments are interpreted through molecular dynamics simulations using the molecular dynamics with alchemical step (MDAS) algorithm for enhanced sampling. Experimental results indicate that the PE content decreases H-bond formation at the ester carbonyl positions near the lipid membrane's hydrophobic core as a result of increased packing density. The observed dehydration is linked to faster molecular dynamics within the interfacial region."

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

DlugSlowWZdaniu(abstrakt) 