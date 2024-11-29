import re

# Tabela translacji kodonów RNA na aminokwasy
table_data = """
UUU F      CUU L      AUU I      GUU V
UUC F      CUC L      AUC I      GUC V
UUA L      CUA L      AUA I      GUA V
UUG L      CUG L      AUG M      GUG V
UCU S      CCU P      ACU T      GCU A
UCC S      CCC P      ACC T      GCC A
UCA S      CCA P      ACA T      GCA A
UCG S      CCG P      ACG T      GCG A
UAU Y      CAU H      AAU N      GAU D
UAC Y      CAC H      AAC N      GAC D
UAA Stop   CAA Q      AAA K      GAA E
UAG Stop   CAG Q      AAG K      GAG E
UGU C      CGU R      AGU S      GGU G
UGC C      CGC R      AGC S      GGC G
UGA Stop   CGA R      AGA R      GGA G
UGG W      CGG R      AGG R      GGG G
"""
slownik = dict(zip(table_data.split()[::2], table_data.split()[1::2]))

# Funkcja do generowania nici komplementarnej
def reverse_complement(seq):
    complement = seq.translate(str.maketrans("ATGC", "TACG"))
    return complement[::-1]

# Funkcja tłumacząca kodony na aminokwasy
def translate_to_protein(rna_seq, slownik):
    codons = [rna_seq[i:i+3] for i in range(0, len(rna_seq), 3)]
    amino_acids = [slownik.get(codon, '-') for codon in codons if codon in slownik]
    return ''.join(amino_acids).replace('Stop', '')

# Funkcja do znajdowania wszystkich sekwencji START-STOP w danej ramce
def find_proteins(dna_seq, slownik):
    proteins = []
    expr = r'ATG(?:[ATGC]{3})*?(?:TAA|TAG|TGA)'
    for frame in range(3):
        # Przesunięcie ramki
        rna_seq = dna_seq[frame:].replace('T', 'U')
        # Znajdowanie dopasowań START-STOP
        matches = re.finditer(expr, rna_seq.replace('U', 'T'))
        for match in matches:
            # Wyciąganie dopasowania i translacja
            match_seq = match.group()
            rna_match = match_seq.replace('T', 'U')
            protein = translate_to_protein(rna_match, slownik)
            if protein:
                proteins.append(protein)
    return proteins

# Przykładowa sekwencja DNA
dna_seq = "AGCCATGTAGCTAACTCAGGTTACATGGGGATGACCCCGCGACTTGGATTAGAGTCTCTTTTGGAATAAGCCTGAATGATCCGAGTAGCATCTCAG"

# Generowanie obu nici DNA
strands = [dna_seq, reverse_complement(dna_seq)]

# Przeszukiwanie obu nici i wszystkich ramek
results = []
for strand_idx, strand in enumerate(strands):
    strand_proteins = find_proteins(strand, slownik)
    results.extend(strand_proteins)

# Wyświetlanie unikalnych wyników
unique_proteins = list(set(results))
for protein in unique_proteins:
    for i in range(len(protein)):
        if(i==0):
            continue
        elif(protein[i]=='M'):
            unique_proteins.append(protein[i:])
print("\n".join(unique_proteins))
