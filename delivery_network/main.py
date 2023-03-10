from graph import Graph, graph_from_file 

data_path = "input/" 
file_name = "network.2.in" 

from time import perf_counter

g=graph_from_file(data_path+file_name)

def machin(filename): 
    f = open("/home/onyxia/work/ensae-prog23/input/"+filename, "r") #On rajoute le début du chemin pour que le programme trouve le chemin du fichier 
    L = f.readlines()#On transforme le tableau en une liste de chaîne de caractères, avec une chaîne = une ligne 
    lignes=[] 
    for i in range(1,len(L)): 
        lignes.append(L[i].split()) #"lignes" est une liste, donc les éléments (qui représentent les lignes de notre tableau) sont des listes de chaînes de caractères 
    return lignes 

def Temps(g, filename):
    L=[]
    lignes = machin(filename)
    for i in range(20):
        l=lignes[i]
        src = l[0] ; dest=l[1]
        t1_start = perf_counter()
        g.min_power(src, dest)
        t1_stop = perf_counter()
        L.append(t1_stop - t1_start)
    S=0
    for l in L:
        S+=l
    Tmoy= S/len(L)
    return Tmoy*(g.nb_nodes-1)*(g.nb_nodes)

print(Temps(g, "routes.2.in")) 
#g=Graph([]) 
#g.add_edge("Paris","Palaiseau",4,20) 
#print(g) 

#A écrire dans le terminal : pip install graphviz