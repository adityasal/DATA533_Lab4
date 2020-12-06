from node import Node

class Tree:
   
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
    
    def inorder(self,node):
        if node is not None:
            self.inorder(node.left)
            print(node.key)
            self.inorder(node.right)
    
    def preorder(self, node):
        if node is not None:
            print(node.key)
            self.preorder(node.left)
            self.preorder(node.right)
    
    def postorder(self, node):
        if node is not None: 
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.key)
