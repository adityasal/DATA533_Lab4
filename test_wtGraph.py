import numpy as np
import pandas as pd
import unittest

from graphsTrees.graphs.graphs import Graph
from graphsTrees.graphs.wtGraphs import wtGraph

class TestwtGraph(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        print('Set up class')
        
    @classmethod
    def tearDownClass(cls):
        print('Tear down class')
    
    def setUp(self):
        print('set up')
        self.Gr1 = wtGraph(5, [[0,1],[1,2],[2,3],[3,4],[4,1],[0,3]], [1,2,3,4,5,6]) #Connected with cycles
        self.Gr2 = wtGraph(3, [[0,1], [2,2]], [5, 7]) # Disconnected with loop cycle
        self.Gr3 = wtGraph(4, [[0,1], [0,2], [0,3]], [2,4,6]) # Connected with no cycles
        self.Gr4 = wtGraph(4, [[0,1],[1,2],[2,3],[3,0],[0,2],[1,3]], [4,9,2,7,1,6]) #Complete graph of 4 vertices
        self.Gr5 = wtGraph(5, [[2,4],[3,4],[2,3],[1,2],[0,4],[1,4]], [1,2,3,4,5,6]) #Challenging for kruskal
        
    def tearDown(self):
        print('Teardown')
        
    def test_add_edge(self):
        self.Gr2.addEdge(1,2,4)
        self.Gr3.addEdge(3,2,7)
        self.assertEqual(self.Gr2.edges, [[0,1], [2,2], [1,2]])
        self.assertEqual(self.Gr2.weights, [5,7,4])
        self.assertEqual(self.Gr3.edges, [[0,1], [0,2], [0,3], [3,2]])
        self.assertEqual(self.Gr3.weights, [2,4,6,7])
        
    def test_rmEdge(self):
        self.Gr1.rmEdge(0,1)
        self.Gr1.rmEdge(2,3)
        self.Gr3.rmEdge(0,3)
        self.assertEqual(self.Gr1.edges, [[1,2], [3,4], [4,1],[0,3]])
        self.assertEqual(self.Gr1.weights, [2,4,5,6])
        self.assertEqual(self.Gr3.edges, [[0,1],[0,2]])
        self.assertEqual(self.Gr3.weights, [2,4])
        
    # Pretty pointless to test this more than once    
    def test_addVertex(self):
        self.Gr1.addVertex()
        np.testing.assert_array_equal(self.Gr1.vertices, np.arange(6))
        
    def test_adjMatrix(self):
        np.testing.assert_array_equal(self.Gr2.adjMatrix(), np.array([[0.,5.,0],
                                                                     [5.,0.,0.],
                                                                     [0.,0.,7.]]))
        
        #I didn't actually realize the matrix was like this when I was building the graph
        np.testing.assert_array_equal(self.Gr1.adjMatrix(), np.array([[0.,1.,0.,6.,0.],
                                                                     [1.,0.,2.,0.,5.],
                                                                     [0.,2.,0.,3.,0.],
                                                                     [6.,0.,3.,0.,4.],
                                                                     [0.,5.,0.,4.,0.]]))
        
        np.testing.assert_array_equal(self.Gr4.adjMatrix(), np.array([[0.,4.,1.,7.],
                                                                     [4.,0.,9.,6.],
                                                                     [1.,9.,0.,2.],
                                                                     [7.,6.,2.,0.]]))
        
#    I had to edit my DFS algorithm to have an output for this to work.
#    Previously it printed the steps and returned None 
    def test_DFS(self):
        self.assertEqual(self.Gr1.DFS(0, showSteps = False), [0,1,2,3,4])
        self.assertEqual(self.Gr1.DFS(2, showSteps = False), [2,1,0,3,4])
        self.assertEqual(self.Gr1.DFS(4, showSteps = False), [4,1,0,3,2])
        self.assertEqual(self.Gr2.DFS(0, showSteps = False), [0,1])
        self.assertEqual(self.Gr2.DFS(2, showSteps = False), [2])
        self.assertEqual(self.Gr3.DFS(0, showSteps = False), [0,1,2,3])
        self.assertEqual(self.Gr3.DFS(2, showSteps = False), [2,0,1,3])
        
    def test_isConnected(self):
        self.assertTrue(self.Gr1.isConnected())
        self.assertTrue(self.Gr3.isConnected())
        self.assertFalse(self.Gr2.isConnected())
        self.assertTrue(self.Gr4.isConnected())
        
    def test_hasCycles(self):
        self.assertTrue(self.Gr1.hasCycles())
        self.assertTrue(self.Gr2.hasCycles())
        self.assertFalse(self.Gr3.hasCycles())
        self.assertTrue(self.Gr4.hasCycles())
        
    def test_kruskal(self):
        self.assertEqual(self.Gr1.kruskal(), [[0,1],[1,2],[2,3],[3,4]])
        self.assertEqual(self.Gr4.kruskal(), [[0,2],[2,3],[0,1]])
        self.assertEqual(self.Gr5.kruskal(), [[2,4],[3,4],[1,2],[0,4]])
        
    def test_totalWeight(self):
        self.assertEqual(self.Gr1.totalWeight(), 21)
        self.assertEqual(self.Gr3.totalWeight(), 12)
        self.assertEqual(self.Gr4.totalWeight(), 29)
        
    unittest.main(argv=[''], verbosity= 2, exit=False)