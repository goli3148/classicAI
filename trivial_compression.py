import sys
class CompressedGene:
    def __init__(self, gene: str) -> None:
        self._compress(gene)
    def _compress(self, gene: str) -> None:
        self.bit_string: int = 1
        for nucleotide in gene.upper():
            self.bit_string <<= 2 
            if nucleotide == "A":
                self.bit_string |= 0b00
            elif nucleotide == "C":
                self.bit_string |= 0b01
            elif nucleotide == "G":
                self.bit_string |= 0b10
            elif nucleotide == "T":
                self.bit_string |= 0b11
            else:
                raise ValueError("Invalid Nucleotide:{}".format(nucleotide))
    def getCompressed(self):
        return self.bit_string

class DecompressGene:
    def __init__(self, bit_string:int) -> None:
        self._decompress(bit_string)
        
    def _decompress(self, bit_string:int)->None:
        self.gene = ""
        for i in range(0, bit_string.bit_length()-1, 2):
            bits = bit_string >> i & 0b11
            if bits == 0b00:
                self.gene += "A"
            elif bits == 0b01:
                self.gene += "C"
            elif bits == 0b10:
                self.gene += "G"
            elif bits == 0b11:
                self.gene += "T"
            else:
                ValueError("Invalid bits:{}".format(bits))
        self.gene = self.gene[::-1]
    
    def getDecompressed(self):
        return self.gene


init_gene = "ACCGGTTATACATGACCGGTTATACATGACCGGTTATACATGACCGGTTATACATG"
bits = CompressedGene(init_gene).getCompressed()
gene = DecompressGene(bits).getDecompressed()

DSize = sys.getsizeof(init_gene)
CSize = sys.getsizeof(bits)
reducedPercent = int((DSize - CSize)/DSize *100)

print(f"{init_gene}->size:{DSize}")
print(f"{bits}->size:{CSize}")
print(f"{gene}->size:{DSize}")

print(f"reduced size is:{reducedPercent}%")