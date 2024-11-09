#zad3
k = open("dataDNA.fasta","r")
data = k.read()
data = data.split(">")
ids = []
for i in range(len(data)):
  if "." in data[i]:
    ids.append(data[i].split("\n")[0])
for i in range(len(data)):
  data[i] = data[i].split("\n")
  data[i] = data[i][1:]
  data[i] = "".join(data[i])
updated_data = list(filter(None, data))
zasady = ['A','T','C','G']
slownik = {}
for i in range(len(ids)):
   slownik[ids[i]] = {'A':0,'T':0,'C':0,'G':0}
b = open("ErrorIDs.txt",'w')
for i in range(len(ids)):
  for znak in updated_data[i]:
    if znak == 'T':
        slownik[ids[i]]['T'] += 1
    elif znak == 'C':
        slownik[ids[i]]['C'] += 1
    elif znak == 'G':
        slownik[ids[i]]['G'] += 1
    elif znak == 'A':
       slownik[ids[i]]['A'] += 1
    else:
        b.write(f"{ids[i]}: zasada nr. {updated_data[i].find(znak)} jest zakodowana niepoprawnie znakiem {znak}\n")
print(slownik)
b.close