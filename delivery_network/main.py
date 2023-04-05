from graph import Graph,function_profit,tri_des_camions,liste_from_file

t=Graph([])
t.add_edge(1,2,7,1)
t.add_edge(1,4,5,1)
t.add_edge(2,4,9,1)
t.add_edge(2,3,8,1)
t.add_edge(3,5,5,1)
t.add_edge(5,7,9,1)
t.add_edge(7,6,11,1)
t.add_edge(5,6,8,1)
t.add_edge(2,5,7,1)
t.add_edge(4,5,15,1)
t.add_edge(4,6,6,1)
'''print(t.new_power_min(6, 5),([6,4,1,2,5],25))
print()'''

print(function_profit("trucks.2.in.txt", "routes.2.in", "network.2.in"))
