from graphsTrees.trees.node import Node

class Tree:
    
    def __init__(self):
        self._preorder_list = []
        self._inorder_list = []
        self._postorder_list = []
   
    def create_node(self,key):
        return Node(key)
    
    def insert(self, node, key):
        if node is None:
            return self.create_node(key)
        else:
            node.left = self.insert(node.left, key)
        return node
    
    def search_node(self,node,key):
        if node is None:
            return "Node {} does not exist".format(key)
        if node.key == key:
            return "Node {} exists".format(key)
        else:
            return self.search_node(node.left,key)
    
    def preorder(self, node):
        if node is not None:
            self._preorder_list.append(node.key)
            self.preorder(node.left)
            self.preorder(node.right)
    
    def inorder(self,node):
        if node is not None:
            self.inorder(node.left)
            self._inorder_list.append(node.key)
            self.inorder(node.right)
    
    def postorder(self, node):
        if node is not None: 
            self.postorder(node.left)
            self.postorder(node.right)
            self._postorder_list.append(node.key)
    
    def get_preorder(self):
        return self._preorder_list
    
    def get_inorder(self):
        return self._inorder_list
    
    def get_postorder(self):
        return self._postorder_list
    
