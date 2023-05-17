import random


def generate_random_codons(n, nuc_list):
    codons = []
    for i in range(n):
        codon = ""
        for j in range(3):
            codon += random.choice(nuc_list)
        codons.append(codon)
    return codons


def remove_invalid(codon_list, invalid_codons):
    choice = input("Do you want to remove invalid codons? (If there is any): ")
    print()

    if choice[0] in ['y', 'Y']:
        invalidCount = 0
        for codon in invalid_codons:
            if codon in codon_list:
                codon_list.remove(codon)
                invalidCount += 1
        if invalidCount > 0:
            print(f"{invalidCount} invalid codons are removed")
            print()
        else:
            print("There are no invalid codons in the list!")
            print()
    return codon_list


def extract_seq_index(codon_list, desired_seq):
    indexes = []
    for i, codon in enumerate(codon_list):
        if desired_seq in codon:
            indexes.append(i)
    return indexes


def main():
    nuc_list = ['A', 'C', 'T', 'G']
    n = int(input("How many random codons do you want to generate?: "))
    print()

    codon_list = generate_random_codons(n, nuc_list)
    print(f"Codon list: {codon_list}")
    print()

    invalid_codons = ['GGA', 'GGT', 'GGG', 'GGC', 'GCA', 'GCT', 'GCC', 'GCG']
    codon_list = remove_invalid(codon_list, invalid_codons)
    print(f"Current codon list = {codon_list}")
    print()

    desired_seq = input("Which nucleotide(s) do you want to search: ")
    print()

    indexes = extract_seq_index(codon_list, desired_seq)
    if indexes:
        print(f"Index(es) of the nucleotide(s) you searched = {indexes}")
    else:
        print("There is no such sequence in the list!")


random.seed(199)
main()
