from graph import Graph, graph_from_file 


data_path = "input/" 
file_name = "network.01.in" 

g = graph_from_file(data_path + file_name) 
print(g.get_path_with_power(1,6,10)) 

#g=Graph([]) 
#g.add_edge("Paris","Palaiseau",4,20) 
#print(g) 