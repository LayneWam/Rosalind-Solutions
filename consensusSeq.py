file = open('rosalind_cons.txt', 'r')
input_string = file.read()
lst = input_string.replace('\n','')
lst = lst.split('>')
lst = list(filter(None,lst))
seqList = []

for i in lst:
        seq = i[13:]
        seqList.append(seq)

n = len(seqList[0])
A, G, C, T = [0]*n, [0]*n, [0]*n, [0]*n

for sequence in seqList:
    for base in range(0, n):
        if sequence[base] == 'A':
            A[base] += 1
        if sequence[base] == 'G':
            G[base] += 1
        if sequence[base] == 'C':
            C[base] += 1
        if sequence[base] == 'T':
            T[base] += 1

seq_max = [0]*n
for i in range(0, n):
        seq_max[i] = max(A[i],C[i],G[i],T[i])
        if seq_max[i] == A[i]:
                seq_max[i] = 'A'
        elif seq_max[i] == C[i]:
                seq_max[i] = 'C'
        elif seq_max[i] == G[i]:
                seq_max[i] = 'G'
        elif seq_max[i] == T[i]:
                seq_max[i] = 'T'
        
print(''.join(seq_max))
print('A: ' + ' '.join(map(str,A)))
print('C: ' + ' '.join(map(str,C)))
print('G: ' + ' '.join(map(str,G)))
print('T: ' + ' '.join(map(str,T)))
