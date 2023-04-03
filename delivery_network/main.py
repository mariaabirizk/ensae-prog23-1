from graph import Graph

t=Graph([])
t.add_edge(1,2,1,1)
t.add_edge(1,5,1,1)
t.add_edge(2,4,1,1)
t.add_edge(2,3,1,1)
"print([t.kruskal().graph[1][i[0]] for i in t.kruskal().graph[1]])"
print([i[0] for i in t.kruskal().graph[1]])
