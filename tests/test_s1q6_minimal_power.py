# This will work if ran from the root folder.
import sys 
sys.path.append("delivery_network")

from graph import Graph, graph_from_file
import unittest   # The test framework

class Test_MinimalPower(unittest.TestCase):
    def test_network0(self):
        g = graph_from_file("input/network.00.in")
        self.assertEqual(g.min_power(1, 4)[1], 11)
        self.assertEqual(g.min_power(2, 4)[1], 10)

    def test_network1(self):
        g = graph_from_file("input/network.04.in")
        self.assertEqual(g.min_power(1, 4)[1], 4)
    
    def test_network5(self):
            t=Graph([])
            t.add_edge(1,7,1,1)
            t.add_edge(1,2,1,1)
            t.add_edge(2,8,1,1)
            t.add_edge(2,3,1,1)
            t.add_edge(3,9,1,1)
            t.add_edge(3,10,1,1)
            t.add_edge(3,4,1,1)
            t.add_edge(4,5,1,1)
            t.add_edge(4,6,1,1)
            t.add_edge(4,1,1,1)
            self.assertEqual(t.min_power(1, 5)[1],1)
    
    def test_network6(self):
            t=Graph([])
            t.add_edge(1,2,2,1)
            t.add_edge(1,3,2,1)
            t.add_edge(1,4,2,1)
            t.add_edge(1,5,2,1)
            t.add_edge(2,3,2,1)
            t.add_edge(2,4,2,1)
            t.add_edge(2,5,2,1)
            t.add_edge(3,4,2,1)
            t.add_edge(3,5,2,1)
            t.add_edge(4,5,1,1)
            self.assertEqual(t.min_power(1, 2)[1],2)
            self.assertEqual(t.min_power(3,4)[1],2)
            self.assertEqual(t.min_power(4, 5)[1],1)

if __name__ == '__main__':
    unittest.main()
