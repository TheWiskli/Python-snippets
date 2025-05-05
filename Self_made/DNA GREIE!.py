dna = "AGCCCTCCAGGACAGGCTGCATCAGAAGAGGCCATCAAGCAGGTCTGTTCCAAGG"

dnatilrna = {
    "A":"U",
    "T":"A",
    "C":"G",
    "G":"C"
}

rna = ""

for i in range(len(dna)):
    base = dna[i]

    rna = rna + dnatilrna[base]


print(rna)