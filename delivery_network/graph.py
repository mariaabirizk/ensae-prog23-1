class Graph: 

    """ 
    A class representing graphs as adjacency lists and implementing various algorithms on the graphs. Graphs in the class are not oriented.  
    Attributes:  
    ----------- 
    nodes: NodeType 
        A list of nodes. Nodes can be of any immutable type, e.g., integer, float, or string. 
        We will usually use a list of integers 1, ..., n. 
    graph: dict 
        A dictionnary that contains the adjacency list of each node in the form 
        graph[node] = [(neighbor1, p1, d1), (neighbor1, p1, d1), ...] 
        where p1 is the minimal power on the edge (node, neighbor1) and d1 is the distance on the edge 
    nb_nodes: int 
        The number of nodes. 
    nb_edges: int 
        The number of edges.  
    """ 
    def __init__(self, nodes=[]): 
        """ 
        Initializes the graph with a set of nodes, and no edges.  
        Parameters:  
        ----------- 
        nodes: list, optional 
            A list of nodes. Default is empty. 
        """ 
        self.nodes = nodes 
        self.graph = dict([(n, []) for n in nodes]) 
        self.nb_nodes = len(nodes) 
        self.nb_edges = 0 
 

    def __str__(self): 
        """Prints the graph as a list of neighbors for each node (one per line)""" 
        if not self.graph: 
            output = "The graph is empty"             
        else: 
            output = f"The graph has {self.nb_nodes} nodes and {self.nb_edges} edges.\n" 
            for source, destination in self.graph.items(): 
                output += f"{source}-->{destination}\n" 
        return output

    def add_edge(self, node1, node2, power_min, dist=1): 
        """ 
        Adds an edge to the graph. Graphs are not oriented, hence an edge is added to the adjacency list of both end nodes.  
        Parameters:  
        ----------- 
        node1: NodeType 
            First end (node) of the edge 
        node2: NodeType 
            Second end (node) of the edge 
        power_min: numeric (int or float) 
            Minimum power on this edge 
        dist: numeric (int or float), optional 
            Distance between node1 and node2 on the edge. Default is 1. 
        """ 
         
         #On vérifie tour à tour si les noeuds sont déjà dans le graphe.
        if node1 not in self.nodes: 
            self.nodes.append(node1) #Si ça n'est pas le cas, on les ajoute aux noeuds...
            self.graph[node1]=[] #... au dictionnaire représentant le graphe pour povoir lui ajouter des voisins...
            self.nb_nodes+=1 #... et enfin on ajoute +1 au nombre de noeuds du graphe.
        
        #On fait de même pour le deuxième noeud
        if node2 not in self.nodes: 
            self.nodes.append(node2) 
            self.graph[node2]=[] 
            self.nb_nodes+=1 
        
        #On déclare ensuite chacun des noeuds comme le voisin de lautre en les ajoutant mutuellement à leurs listes de voisins.
        self.graph[node1].append((node2,power_min,dist)) 
        self.graph[node2].append((node1,power_min,dist)) 
        
        #Et enfin, on ajoute +1 au nombre d'arêtes du graphe.
        self.nb_edges+=1 
    
    #On implémente une fonction auxiliaire récursive explorer1, qui servira pour la fonction get_path_with_power.
    #'ville' et 'dest' sont deux villes ('dest' est la destination entrée dans get_path_with_power).
    #'visite' est la liste des villes déjà visitées.
    #'power' est la puissance entrée dans get_path_with_power.
    #'trajet' contient la liste des villes qui forment le trajet en cours, partant de la ville de départ ('src').
    
    def explorer1(self,ville,dest,visite,power,trajet):
        if ville==dest: #On se place dans le cas dans lequel on arrive à destination.
            return trajet #On renvoie le trajet effectué, qui est un trajet effectif pour reliser 'src' à 'dest'.
        
        visite.append(ville) #On déclare 'ville' comme un ville visitée.
        voisins_de_ville=self.graph[ville] #On pose une nouvelle liste de listes, dont chaque premier élément est le numéro d'un voisin de 'ville'.
        
        for voisin in voisins_de_ville: #On parcourt tous les voisins de 'ville'.
            
            if voisin[0] not in visite and power>=voisin[1]: #On se place dans le cas où la ville voisine n'a pas été visitée, et la puissance du camion est assez grande pour passer par cette arête.
                trajet.append(voisin[0]) #On ajoute alors le voisin au trajet.
                resultat = self.explorer1(voisin[0],dest,visite,power,trajet)
                if resultat is not None: #On se place dans le cas où passer par cette ville ne nous empêche pas de rallier 'dest' et 'src'.
                    return resultat 
                else: #On se place dans le cas où on ne parvient pas à rallier 'dest' et 'src' en passant par 'voisin[0]'
                    trajet.pop() #Dans ce cas, on enlève simplement 'voisin[0]' (le dernier élément du trajet) du trajet. On ne rebouclera pas car désormais, voisin[0] est dans 'visite'.
       
        return None #Si on arrive ici, c'est que tous les voisins de 'ville' ont soit déjà été visités sans succès, soit que le camion ne pourra y accéder en passant par 'ville'. Il a donc été impossible de relier 'src' et 'dest' en passant par 'voisin' : on renvoie 'None'.

    #On passe à la fonction en elle-même.
    def get_path_with_power(self, src, dest, power):
        
        #On cherche la composante connexe de 'src'. 
        W=[]
        for l in self.connected_components(): #l est un element de la liste obtenu par la meth comp 
            if src in l:
                W=l
        #Comme 'self.connected_components()' est une partition des noeuds du graphe, il y aura forcément un et un seul 'l' dans 'self.connected_components()' tel que 'W=l'.

        if dest in W : #On se place dans le cas où 'src' et 'dest' sont dans la même composante connexe.
            visite=[] #On initialise les voisins visités de 'src' à l'ensemble vide.
            trajet=[src] #On initialise le trajet pour qu'il commence toujours par 'src'.
            return self.explorer1(src,dest,visite,power,trajet) #On utilise la fonction auxiliaire définie ci-dessus.
        
        else : #On se place dans le cas où 'src' et 'dest' ne sont pas dans la même composante connxe, c'est-à-dire qu'il n'existe même pas de chemin les reliant (indépendamment de la puissance).
            return None
     

    
    #On implémente une fonction récusrive annexe explorer2 pour connected_components. 
    #'i' est un numéro de noeud.
    #'visited' est un dictionnaire associant à chaque noeud du graphe un booléen ('True' s'il a déjà été visité, 'False' sinon). 
    def explorer2(self,i,visited):
            L=[] #'L' est une liste représentant la composante connexe de 'i'.
            if self.graph[i]==[]: #Si 'i' n'a aucun voisin... 
                L=[i] #... alors la composante connexe n'est composée que du noeud 'i'.
            
            for W in self.graph[i]: 
                if visited[W[0]]==False :
                    visited[W[0]]=True
                    L.append(W[0])
                    L=L+self.explorer2(W[0], visited)
            return L
 
    def connected_components(self):  
        U=[]
        f={}
        for W in self.graph :
            f[W]=False      
        for i in self.graph:
            L=self.explorer2(i,f)
            if L!=[]:
                U.append(L)
        return (U)
    #Calcul de complexité à effectuer
 
    def connected_components_set(self): 
        """ 
        The result should be a set of frozensets (one per component),  
        For instance, for network01.in: {frozenset({1, 2, 3}), frozenset({4, 5, 6, 7})} 
        """ 
        return set(map(frozenset, self.connected_components())) 
     
    def min_power(self, src, dest): 
        """ 
        Should return path, min_power.  
        """
         #prob avec graph[cle] mafine
        maxi=0
        for voisins in self.graph[src]:
            if voisins[1]>maxi :
                maxi=voisins[1]  #je ne vais pas faire ca pour min pour ne pas reparcourir if

        puissance_min = 0
        puissance_max = maxi
        chemin=[]
        while puissance_min < puissance_max:
            puissance = (puissance_min + puissance_max) // 2
            if self.get_path_with_power(src, dest, puissance) is not None: #cad si c est un des chemins possible j'essaie de voir s'il ya un pour une plus petite puiss
                puissance_max = puissance
                
            else:
                puissance_min = puissance + 1  #on augmente la puiss pour arriver a une puisssance efficace

        chemin=self.get_path_with_power(src,dest,puissance_max) #on retourne le chemin pr la puiss
        return (chemin, puissance_max)
 

#Cette fonction ne marche qu'avec des tableaux d'entiers, comme dans les fichiers proposés
def graph_from_file(filename): 
    f = open("/home/onyxia/work/ensae-prog23/"+filename, "r") #On rajoute le début du chemin pour que le programme trouve le chemin du fichier 
    L = f.readlines()#On transforme le tableau en une liste de chaîne de caractères, avec une chaîne = une ligne 
    lignes=[] 
    g=Graph([]) 
    for i in range(1,len(L)): 
        lignes.append(L[i].split()) #"lignes" est une liste, donc les éléments (qui représentent les lignes de notre tableau) sont des listes de chaînes de caractères 
    for line in lignes: 
        if len(line)==3: 
            g.add_edge(int(line[0]),int(line[1]),int(line[2]),1) 
        else : 
            g.add_edge(int(line[0]),int(line[1]),int(line[2]),int(line[3])) 
    #Attention ! Tous les sommets ne sont pas forcément reliés à d'autres sommets ! Dans cette partie du code, on s'occupe de mettre dans le graphe les sommets isolés 
    nb_nodes=int(L[0].split()[0]) #Le nombre de sommets est donné par le premier nombre de la première ligne 
    for n in range(1,nb_nodes+1): #On suppose ici que s'il y a n noeuds, tous les noeuds sont exactement tous les numéros de 1 à n. 
        if n not in g.graph: 
            g.graph[n]=[] 
            g.nb_nodes+=1 #Le nombre d'arêtes n'a pas été modifié, mais le nombre de sommets a lui changé 
    return g 

'''def kruskal(g) :
    g_mst=Graph([])
    #Trier les arêtes du graphe 
    for u
    for arêtes in ensemble_des_arêtes_trié :
        if u !=v :
            g_mst.add_edge(u, v, truc)

    return (g_mst)'''