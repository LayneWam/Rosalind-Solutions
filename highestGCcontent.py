def dictionary(string):
    lst = string.replace('\n','')
    lst = lst.split('>')
    lst = list(filter(None,lst))
    dct = {}
    for seq in lst:
        seq_id = seq.split('_')[1][:4]
        seq_value = seq.split('_')[1][4:]
        dct['Rosalind_' + seq_id] = seq_value
    return dct

def calcContent():
    dct = dictionary(input_string)
    seq, counter = 0, 0
    for seq_id, seq_values in dct.items():
        GC = seq_values.count('G') + seq_values.count('C')
        total = len(seq_values)
        percent =(GC/total)*100
        if percent > counter:
            counter = percent
            seq = seq_id
    return seq, counter

file = open("rosalind_gc.txt", "r")
input_string = file.read()
seq, counter = calcContent()
print(seq, counter)
