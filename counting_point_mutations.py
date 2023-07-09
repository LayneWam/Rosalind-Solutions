file = open("rosalind_hamm.txt", "r")
input_string = file.read()

lst = input_string.split("\n")
s = str(lst[0])
t = str(lst[1])
dist = 0

for i in range(0,len(s)):
    if s[i] != t[i]:
        dist += 1

print(dist)
