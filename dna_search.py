from enum import IntEnum
from typing import Tuple, List

Nucleotide: IntEnum = IntEnum('Nucleotide', ('A', 'C', 'G', 'T'))
Codon = Tuple[Nucleotide, Nucleotide, Nucleotide]
Gene = List[Codon]

def string_to_gene(s: str) -> Gene:
    gene: Gene = []
    for i in range(0, len(s), 3):
        if (i+2) >= len(s):
            return gene
        codon: Codon = (Nucleotide[s[i]], Nucleotide[s[i+1]], Nucleotide[s[i+2]])
        gene.append(codon)
    return gene

def linear_contains(gene: Gene, key: Codon)->bool:
    for codon in gene:
        if codon == key:
            return True
    return False

def binary_contains(gene: Gene, key: Codon):
    low: int = 0
    high: int = len(gene)-1
    while low<=high:
        mid: int = (high+low)//2
        if gene[mid] > key:
            high = mid + 1
        elif gene[mid] < key:
            low = mid -1
        else:
            return True
    return False
    

# TEST
print("RUNTIME -------------------------------------------------------------------------")
gene_str: str = "ATGTGGCTCTCTAACGTACGTACGTACGGGGTTTATATATACCCTAGGACTCCCTTT"
my_gene: Gene = string_to_gene(gene_str)
# for i in my_gene:
#     print(i)
atg: Codon = (Nucleotide.A, Nucleotide.T, Nucleotide.G)
acg: Codon = (Nucleotide(1), Nucleotide(2), Nucleotide(3))
print("linear serach: ATG: ",linear_contains(my_gene, atg))
print("linear search: ACG: ",linear_contains(my_gene, acg))

sorted_gene: Gene = sorted(my_gene)

print("binary search: ATG: ", binary_contains(sorted_gene, atg))
print("binary search: ACG: ", binary_contains(sorted_gene, acg))