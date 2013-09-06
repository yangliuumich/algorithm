#median maintainence
filename = "Median.txt"
with open(filename) as f:
    graph = [int(i) for i in f.read().splitlines()]

def get_median(l):
    array = l
    array.sort()
    n = len(array)
    if n % 2 == 0:
        return array[int(n/2-1)]
    else:
        return array[n//2]

sum_median = 0
for i in range(1,10001):
    sum_median += get_median(graph[:i])

print(sum_median % 10000)
