import unittest

from graphsTrees.trees.node import Node
from graphsTrees.trees.tree import Tree
from graphsTrees.trees.bst import BST
from graphsTrees.exceptions.TreeExceptions import NodeError,NodeKeyError

class TestBST (unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        print('Set Up Class')
    
    @classmethod 
    def tearDownClass(cls):
        print('Tear Down Class')
    
    def setUp(self):
        print('Set Up')
        self.bst1 = BST()
        self.bst2 = BST()
        self.bst3 = BST()
        self.bst4 = BST()
        self.bst5 = BST()
        self.bst6 = BST()
        self.bst7 = BST()
        
        
    def tearDown(self):
        print('Teardown')
    
    def test_create_node(self):
        bst1_root_node = self.bst1.create_node(5)
        bst1_root_node.left = 11
        
        self.assertIsInstance(self.bst1,BST)
        self.assertIsInstance(bst1_root_node,Node)
        self.assertEqual(bst1_root_node.key,5)
        self.assertEqual(bst1_root_node.left,11)
    
    def test_insert(self):
        bst2_root_node = self.bst2.create_node(10)
        self.bst2.insert(bst2_root_node,23)
        self.bst2.insert(bst2_root_node,0)
        
        self.assertIsInstance(self.bst2,BST)
        self.assertIsInstance(bst2_root_node,Node)
        self.assertEqual(bst2_root_node.right.key,23)
        self.assertEqual(bst2_root_node.left.key,0)
    
    def test_search_node(self):
        bst3_root_node = self.bst3.create_node(1)
        self.bst3.insert(bst3_root_node,15)
        
        self.assertIsInstance(self.bst3,BST)
        self.assertIsInstance(bst3_root_node,Node)
        self.assertEqual(self.bst3.search_node(bst3_root_node,15),"Node 15 exists")
        self.assertEqual(self.bst3.search_node(bst3_root_node,0),"Node 0 does not exist")
    
    def test_delete_node(self):
        bst4_root_node = self.bst4.create_node(10)
        self.bst4.insert(bst4_root_node,23)
        self.bst4.insert(bst4_root_node,0)
        
        self.assertIsInstance(self.bst4,BST)
        self.assertIsInstance(bst4_root_node,Node)
        self.assertEqual(bst4_root_node.right.key,23)
        self.assertEqual(bst4_root_node.left.key,0)    
        
        self.bst4.delete_node(bst4_root_node,23)
        
        self.assertEqual(bst4_root_node.right,None)
        self.assertEqual(bst4_root_node.left.key,0)  
    
    def test_preorder(self):
        bst5_root_node = self.bst5.create_node(10)
        self.bst5.insert(bst5_root_node,23)
        self.bst5.insert(bst5_root_node,0)
        
        self.bst5.preorder(bst5_root_node)
        
        self.assertIsInstance(self.bst5,BST)
        self.assertIsInstance(bst5_root_node,Node)
        self.assertIsInstance(self.bst5.get_preorder(),list)
        self.assertEqual(self.bst5.get_preorder(),[10, 0, 23])
    
    def test_inorder(self):
        bst6_root_node = self.bst6.create_node(10)
        self.bst6.insert(bst6_root_node,23)
        self.bst6.insert(bst6_root_node,0)
        
        self.bst6.inorder(bst6_root_node)
        
        self.assertIsInstance(self.bst6,BST)
        self.assertIsInstance(bst6_root_node,Node)
        self.assertIsInstance(self.bst6.get_inorder(),list)
        self.assertEqual(self.bst6.get_inorder(),[0, 10, 23])
    
    def test_postorder(self):
        bst7_root_node = self.bst7.create_node(10)
        self.bst7.insert(bst7_root_node,23)
        self.bst7.insert(bst7_root_node,0)
        
        self.bst7.postorder(bst7_root_node)
        
        self.assertIsInstance(self.bst7,BST)
        self.assertIsInstance(bst7_root_node,Node)
        self.assertIsInstance(self.bst7.get_postorder(),list)
        self.assertEqual(self.bst7.get_postorder(),[0, 23, 10])


