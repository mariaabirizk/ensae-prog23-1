from graph import Graph, graph_from_file 


data_path = "input/" 
file_name = "network.03.in" 

g = graph_from_file(data_path + file_name) 
print(g.get_path_with_power(1,4,11)) 
print(g)

#g=Graph([]) 
#g.add_edge("Paris","Palaiseau",4,20) 
#print(g) 