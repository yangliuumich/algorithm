#compute strongly connected components
import sys
import threading
threading.stack_size(2**27)
sys.setrecursionlimit(10**9)
filename = "SCC.txt"
with open(filename) as f:
    g = f.read().splitlines()

graph_dict = {}

for line in g:
    node_pair = line.split()
    node_pair = [int(i) for i in node_pair]
    source_node = node_pair[0]
    destination_node = node_pair[1]
    if destination_node not in graph_dict:
            graph_dict[destination_node] = []
    if source_node in graph_dict:
        graph_dict[source_node].append(destination_node)
    else:
        graph_dict[source_node] = [destination_node]

graph_rev_dict = {}
for line in g:
    node_pair = line.split()
    node_pair = [int(i) for i in node_pair]
    source_node = node_pair[1]
    destination_node = node_pair[0]
    if destination_node not in graph_rev_dict:
            graph_rev_dict[destination_node] = []
    if source_node in graph_rev_dict:
        graph_rev_dict[source_node].append(destination_node)
    else:      
        graph_rev_dict[source_node] = [destination_node]

def init():
    explored = {}
    leader = {}
    f = {}
    t = 0
    s = None
    for i in range(1, len(graph_dict)+1):
        explored[i] = False
        leader[i] = None
        f[i] = 0
    return explored, leader, f, t, s

def DFS_loop(graph):
    global s
    for i in range(len(graph), 0, -1):
        if not explored[i]:
            s = i
            DFS(graph, i)


def DFS(graph, i):
    global s, t
    explored[i] = True
    leader[i] = s
    for j in graph[i]:
        if not explored[j]:
            DFS(graph, j)
    t += 1
    f[i] = t

def n_max(leader, n):
    counting = {}
    for key in leader:
        if leader[key] not in counting:
            counting[leader[key]] = 1
        else:
            counting[leader[key]] += 1
    result = [counting[key] for key in counting]
    result.sort(reverse=True)
    if len(counting) >= n:
        return result[:n]
    else:
        while(len(result)<n):
            result.append(0)
        return result
        
        
    
explored, leader, f, t, s = init()
DFS_loop(graph_rev_dict)
graph_new_dict = {}
for key in graph_dict:
    graph_new_dict[f[key]] = [f[i] for i in graph_dict[key]]

explored, leader, f, t, s = init()
DFS_loop(graph_new_dict)
print(n_max(leader, 5))

if __name__ == '__main__':
    thread = threading.Thread(target=main)
    thread.start()
