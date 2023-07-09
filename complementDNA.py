
def swapLetters(seq):
    table = str.maketrans('ATCG','TAGC')
    out = seq.translate(table)
    return out

seq = str(input(''))
out = swapLetters(seq)
print(out[::-1])
