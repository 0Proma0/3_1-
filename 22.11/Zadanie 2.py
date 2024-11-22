class Seq():
    def __init__(self,seq_id,seq):
        self.seq_id = seq_id
        self.seq = seq

    def __len__(self):
        return len(self.seq)

    def __str__(self):
        return self.seq

    @classmethod
    def from_file(cls, filename):
        seq_list = []
        with open(filename) as f:
            data = f.read()
        raw = [x for x in data.split(">")][1:]
        seqs = [seq.split("\n",maxsplit=1)[1].replace("\n",'') for seq in raw]
        seq_id = [acc.split(' ',maxsplit=1)[0] for acc in raw]
        for temp_id,seq in zip(seq_id,seqs):
            seq_list.append(cls(temp_id,seq))
        return seq_list


class RNASeq(Seq):
    pozw_znaki = {"A","U","C","G"}
    def __init__(self,seq_id,seq,):
        super().__init__(seq_id, seq)
        for znak in self.seq:
            if(znak!="A" and znak!="U" and znak!="C" and znak!="G"):
                print("Sekwencja zawiera niepozwolone znaki!")
                return TypeError

    def countGC(self):
        return self.seq.count("G")+self.seq.count("C")
    
class DNASeq(Seq):
    pozw_znaki = {"A","T","C","G"}
    def __init__(self,seq_id,seq):
        super().__init__(seq_id, seq)
        for znak in self.seq:
            if(znak!="A" and znak!="T" and znak!="C" and znak!="G"):
                print("Sekwencja zawiera niepozwolone znaki!")
                return TypeError

    def transcribe(self):
        return self.seq.replace("T","U")
