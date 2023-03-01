def check(dna):
    for nucleotide in dna:
        if nucleotide not in 'ATGC':
            print('Invalid DNA')
            return True
    return False

def main():
    dna = input().strip().upper()
    mode = input().strip() 

    if mode == 'R':
        if check(dna): return
        dna_map = ['A', 'T', 'A', 'C', 'G', 'C']
        print("".join([dna_map[dna_map.index(nucleotide) + 1] for nucleotide in dna])[::-1])
        return

    elif mode == 'F':
        if check(dna): return
        print('A='+str(dna.count('A'))+', '+'T='+str(dna.count('T'))+', '+'G='+str(dna.count('G'))+', '+'C='+str(dna.count('C')))
        return
    
    elif mode == 'D':
        if check(dna): return
        interested_pair = input().strip()
        count = 0
        for i in range(1, len(dna)):
            if dna[i-1]+dna[i] == interested_pair:
                count += 1
        print(count)
        return
main()