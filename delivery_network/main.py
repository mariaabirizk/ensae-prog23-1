from graph import Graph, graph_from_file, Temps

data_path = "input/" 
file_name = "network.2.in" 


g=graph_from_file(data_path+file_name)





print(Temps(g, "routes.2.in")) 
#g=Graph([]) 
#g.add_edge("Paris","Palaiseau",4,20) 
#print(g) 
