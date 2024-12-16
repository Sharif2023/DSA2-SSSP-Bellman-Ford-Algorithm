def bellman_ford(graph,source):
    distances = {}
    predecessor = {}

    #init all distance to infinity and predecessor to to null
    for node in graph:
        distances[node] = float('inf')
        predecessor[node] = None
    #init source to zero
    distances[source] = 0

    #Relax edges |V| - 1 times
    for _ in range(len(graph)-1):
        for u in graph:
            for v in graph[u]:
                if distances[v] > distances[u]+graph[u][v]:
                    distances[v] = distances[u]+graph[u][v]
                    predecessor[v] = u

    #check negative-weight cycles
    for u in graph:
        for v in graph[u]:
            if distances[v]>distances[u]+graph[u][v]:
                print("Graph contains negative cycle")
                return None

    return distances

graph = {
    'z':{'a':6,'x':7},
    'a':{'b':5,'x':8,'y':-4},
    'b':{'a':-2},
    'x':{'b':-3,'y':9},
    'y':{'z':2,'b':7}
}
source = 'z'
shortest_distances = bellman_ford(graph,source)
if shortest_distances:
    print(shortest_distances)

def main():
    bellman_ford(graph,source)

if __name__ == '__main__':
    main()