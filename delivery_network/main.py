from graph import Graph, graph_from_file 

data_path = "input/" 
file_name = "network.00.in" 

g = graph_from_file(data_path + file_name) 
print(g.get_path_with_power(1, 4, 10), [1, 2, 3, 4]) 
#g=Graph([]) 
#g.add_edge("Paris","Palaiseau",4,20) 
#print(g) 

#A écrire dans le terminal : pip install graphviz