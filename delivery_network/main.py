from graph import Graph,function_profit,tri_des_camions,liste_from_file, function_profit_exacte
'''
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
'''
'''print(t.kruskal().min_power_arbre(6, 7, 1, t.kruskal().creer_parents(1)))'''

print(function_profit("trucks.1.in.txt", "routes.1.in", "network.1.in"))
