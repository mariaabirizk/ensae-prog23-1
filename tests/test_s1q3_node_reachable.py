# This will work if ran from the root folder.
import sys 
sys.path.append("delivery_network")

from graph import Graph, graph_from_file

import unittest   # The test framework

class Test_Reachability(unittest.TestCase):
    def test_network0(self):
        g = graph_from_file("input/network.00.in")
        self.assertEqual(g.get_path_with_power(1, 4, 11), [1, 2, 3, 4])
        self.assertEqual(g.get_path_with_power(1, 4, 10), None)

    def test_network2(self):
        g = graph_from_file("input/network.02.in")
        self.assertIn(g.get_path_with_power(1, 2, 11), [[1, 2], [1, 4, 3, 2]])
        self.assertEqual(g.get_path_with_power(1, 2, 5), [1, 4, 3, 2])

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
            self.assertIn(t.get_path_with_power(1, 5, 1), [[1, 2, 3, 4, 5], [1,4,5]])
            self.assertEqual(t.get_path_with_power(1, 5, 0),None)
            self.assertIn(t.get_path_with_power(10, 7, 1),[[10,3,2,1,7],[10,3,4,1,7]])

if __name__ == '__main__':
    unittest.main()
