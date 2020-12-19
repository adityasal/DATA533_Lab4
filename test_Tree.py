import unittest
import pytest

from graphsTrees.trees.node import Node
from graphsTrees.trees.tree import Tree
from graphsTrees.exceptions.TreeExceptions import NodeError,NodeKeyError

class TestTree (unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        print('Set Up Class')
    
    @classmethod 
    def tearDownClass(cls):
        print('Tear Down Class')
    
    def setUp(self):
        print('Set Up')
        self.t1 = Tree()
        self.t2 = Tree()
        self.t3 = Tree()
        
    def tearDown(self):
        print('Teardown')
    
    def test_create_node(self):
        t1_root_node = self.t1.create_node(5)
        t1_root_node.left = 11
        
        self.assertIsInstance(self.t1,Tree)
        self.assertIsInstance(t1_root_node,Node)
        self.assertEqual(t1_root_node.key,5)
        self.assertEqual(t1_root_node.left,11)
        
        with pytest.raises(NodeKeyError):
            self.t1.create_node('a')
        
    
    def test_insert(self):
        t2_root_node = self.t2.create_node(10)
        self.t2.insert(t2_root_node,23)
        self.t2.insert(t2_root_node,0)
        
        self.assertIsInstance(self.t2,Tree)
        self.assertIsInstance(t2_root_node,Node)
        self.assertEqual(t2_root_node.left.key,23)
        self.assertEqual(t2_root_node.left.left.key,0)
    
    def test_search_node(self):
        t3_root_node = self.t3.create_node(1)
        self.t3.insert(t3_root_node,15)
        
        self.assertIsInstance(self.t3,Tree)
        self.assertIsInstance(t3_root_node,Node)
        self.assertEqual(self.t3.search_node(t3_root_node,15),"Node 15 exists")
        self.assertEqual(self.t3.search_node(t3_root_node,0),"Node 0 does not exist")
        
        with pytest.raises(NodeKeyError):
            self.t3.search_node(t3_root_node,'a')



