string = input('Enter: ')
strList = string.split(' ')

n = int(strList[0])
m = int(strList[1])

seq = []

new = 1
ready = 0
old = 0
elderly = 0
for i in range(0, n):
    elderly = old
    old = ready
    ready = new
    nextNum = ready + seq[-1] - elderly
    n = nextNum
    seq.append(nextNum)

print(seq[-1])
