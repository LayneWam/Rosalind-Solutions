string = input('Enter: ')
strList = string.split(' ')

n = int(strList[0])
k = int(strList[1])

seq = [1,1]

for i in range(2, n):
    nextNum = seq[i-2]*k + seq[i-1]
    seq.append(nextNum)


print(seq[-1])
