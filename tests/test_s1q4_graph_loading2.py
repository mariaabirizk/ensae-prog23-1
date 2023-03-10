# À compléter

import sys 
sys.path.append("delivery_network/")

import unittest 
from graph import Graph, graph_from_file

class Test_Reachability(unittest.TestCase):
    def test_network4(self):
        g = graph_from_file("input/network.04.in")
        self.assertEqual(set(g.graph[1]), set([(4,11,6),(2,4,89)]))
        self.assertEqual(set(g.graph[3]), set([(2,4,3),(4,4,2)]))


if __name__ == '__main__':
    unittest.main()