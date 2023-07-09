input_string = input('Enter composition: ')
lst = input_string.split(' ')
lst = list(map(int, lst))
k, m, n = lst[0], lst[1], lst[2]
total = sum(lst)
AaAa = (m/total)*((m-1)/(total-1))*(1/4)
aaaa = (n/total)*((n-1)/(total-1))
Aaaa = (m/total)*(n/(total-1))*(1/2)
aaAa = (m/total)*(n/(total-1))*(1/2)

prob_unfav = AaAa + aaaa + Aaaa + aaAa

prob_fav = 1-prob_unfav

print(round(prob_fav,5))

