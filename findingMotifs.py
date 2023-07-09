s = input('Enter full sequence: ')
t = input('Enter test string: ')
lst = [i+1 for i in range(len(s)) if s.startswith(t, i)]
print(' '.join(map(str,lst)))
