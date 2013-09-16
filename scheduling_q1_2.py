#question 1: schedule jobs in decreasing order of difference
filename = 'jobs.txt'
#filename = 'scheduling_test.txt'
with open(filename) as f:
    g = f.read().splitlines()

graph = {}
#graph[key] = [weight, length, w-l, w/l]
for i in range(1, int(g[0])+1):
    w_l = [int(u) for u in g[i].split(' ')]
    graph[i] = w_l + [w_l[0] - w_l[1]] + [w_l[0]/float(w_l[1])]

def order(graph, method):
    #graph.items() = [(key, [weight, length, difference, ratio]), ()...]
    l = graph.items()    
    if method == 'difference':
        m = 2
    elif method == 'ratio':
        m = 3
    else:
        print 'method not found'
    l.sort(key = lambda element: (element[1][m], element[1][0]), reverse = True)
    return l

def weighted_complete_time(sorted_l):
    weighted = 0
    completed = 0
    for (key, [w,l,d,r]) in sorted_l:
        completed += l
        weighted += w * completed
    print weighted

for method in ['difference', 'ratio']:
    weighted_complete_time(order(graph, method))
