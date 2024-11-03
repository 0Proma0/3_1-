import ast
def Funkcja(*NazwyPlikow, **Szyfr):
    szyfr_ascii = {ord(k): ord(v) for k,v in Szyfr.items()}
    for Plik in NazwyPlikow:
        with open(Plik, "r") as p:
            with open(f"Zaszyfrowany_{Plik}", "w+") as s:
                tekst = p.read()
                s.write(tekst.translate(szyfr_ascii))
Szyfr = ast.literal_eval(open("Szyfr.txt","r").read())
Funkcja("Tekst1.txt","Tekst2.txt",**Szyfr)

# Opis programu:
# Użytkownik przygotowuje dowolną liczbę plików .txt do zaszyfrowania i plik Szyfr.txt w którym zapisuje w potaci słownika zasady szyfrowania gdzie klucz i wartość to jednoliterowe elementy
# Nastepnie użytkownik wywołuje funkcje i jako wynik zostają wygenerowane pliki Zaszyfrowany_{nazwa pliku}.txt, którego kluczem jest słownik z Szyfr.txt
# Program może być użyty np. do przetłumaczenia nici DNA na RNA oraz nić komplementarną