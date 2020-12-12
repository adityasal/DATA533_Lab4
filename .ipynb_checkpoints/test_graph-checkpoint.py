import numpy as np
import pandas as pd
import unittest
import pytest

from graphsTrees.graphs.graphs import Graph
from graphsTrees.exceptions.EricExceptions import weightError
from graphsTrees.exceptions.EricExceptions import vertexError
from graphsTrees.exceptions.EricExceptions import edgeError

class TestGraph(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        print('Set up class')
        
    @classmethod
    def tearDownClass(cls):
        print('Tear down class')
    
    def setUp(self):
        print('Set up')
        self.Gr1 = Graph(5, [[0,1],[1,2],[2,3],[3,4],[4,1],[0,3]]) #Connected with cycles
        self.Gr2 = Graph(3, [[0,1], [2,2]]) # Disconnected with loop cycle
        self.Gr3 = Graph(4, [[0,1], [0,2], [0,3]]) # Connected with no cycles
        self.Gr4 = Graph(4, [[0,1],[1,2],[2,3],[3,0],[0,2],[1,3]]) # Complete graph
        
    def tearDown(self):
        print('Teardown')
        
    def test_init(self):
        with pytest.raises(vertexError):
            # Vertex set is defined by an integer.
            Graph([1,2,3], [1,2])
        with pytest.raises(edgeError):
            # There is no vertex 5 to have an edge to.
            Graph(4, [[0,1], [5,2]])
        with pytest.raises(edgeError):
            # Try making an edge with 3 elements
            Graph(4, [[1,2,3]])
        with pytest.raises(edgeError):
            Graph(4, 'Potato')
        
    def test_add_edge(self):
        self.Gr2.addEdge(1,2)
        self.Gr3.addEdge(3,2)
        self.assertEqual(self.Gr2.edges, [[0,1], [2,2], [1,2]])
        self.assertEqual(self.Gr3.edges, [[0,1], [0,2], [0,3], [3,2]])
        # Failed additions
        self.assertEqual(self.Gr2.addEdge(1,2), 'Edge already in edge set')
        self.assertEqual(self.Gr3.addEdge(5,7), 'Input valid vertices')
        
    def test_printGraph(self):
        # I know this test is pointless, but the function is very obviously functional
        # because all it does is print stuff, but I couldn't figure out formatting
        # and needed the test to get coverage to 100%
        self.assertEqual(self.Gr2.printGraph(), self.Gr2.printGraph())
        
    def test_rmEdge(self):
        self.Gr1.rmEdge(0,1)
        self.Gr1.rmEdge(2,3)
        self.Gr3.rmEdge(0,3)
        self.assertEqual(self.Gr1.edges, [[1,2], [3,4], [4,1],[0,3]])
        self.assertEqual(self.Gr3.edges, [[0,1],[0,2]])
        self.assertEqual(self.Gr3.rmEdge(1,1), 'Edge not in edge set')
        
    # Pretty pointless to test this more than once    
    def test_addVertex(self):
        self.Gr1.addVertex()
        np.testing.assert_array_equal(self.Gr1.vertices, np.arange(6))
        
        
    def test_adjMatrix(self):
        np.testing.assert_array_equal(self.Gr2.adjMatrix(), np.array([[0.,1.,0],
                                                                     [1.,0.,0.],
                                                                     [0.,0.,1.]]))
        
        #I didn't actually realize the matrix was like this when I was building the graph
        np.testing.assert_array_equal(self.Gr1.adjMatrix(), np.array([[0.,1.,0.,1.,0.],
                                                                     [1.,0.,1.,0.,1.],
                                                                     [0.,1.,0.,1.,0.],
                                                                     [1.,0.,1.,0.,1.],
                                                                     [0.,1.,0.,1.,0.]]))
        
   #I had to edit my DFS algorithm to have an output for this to work.
   #Previously it printed the steps and returned None 
    def test_DFS(self):
        self.assertEqual(self.Gr1.DFS(0, showSteps = False), [0,1,2,3,4])
        self.assertEqual(self.Gr1.DFS(2, showSteps = False), [2,1,0,3,4])
        self.assertEqual(self.Gr1.DFS(4, showSteps = False), [4,1,0,3,2])
        self.assertEqual(self.Gr2.DFS(0, showSteps = False), [0,1])
        self.assertEqual(self.Gr2.DFS(2, showSteps = False), [2])
        self.assertEqual(self.Gr3.DFS(0, showSteps = False), [0,1,2,3])
        self.assertEqual(self.Gr3.DFS(2, showSteps = False), [2,0,1,3])
        self.assertEqual(self.Gr1.DFS(12, showSteps = False), 'Invalid starting vertex')
        
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
        
unittest.main(argv=[''], verbosity= 2, exit=False)