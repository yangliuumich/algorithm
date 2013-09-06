#2-SUM new version
filename = 'prob-2sum.txt'
with open(filename) as f:
    graph = [int(i) for i in f.read().splitlines()]

h_table = {}
for i in graph:
    if i // 20000 not in h_table:
        h_table[i//20000] = [i]
    else:
        if i not in h_table[i//20000]:
            h_table[i//20000] += [i]

distinct = 0
for t in range(-10000,10001):
    count = 0
    for key in h_table:
        for x in h_table[key]:
            if (t - x)//20000 in h_table:
                if t - x in h_table[(t-x)//20000]:
                    count += 1
    if count == 1:
        distinct += 1

print (distinct)
