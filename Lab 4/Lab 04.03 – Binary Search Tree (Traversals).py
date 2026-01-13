"""Lab 04.03 – Binary Search Tree (Traversals)"""
class BSTNode:
    def __init__(self, data: int=None):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, data, node=None):
        if self.root is None:
            self.root = BSTNode(data)
            return

        if node is None:
            node = self.root
        
        if data < node.data:
            if node.left is None:
                node.left = BSTNode(data)
            else:
                self.insert(data, node.left)
        else:
            if node.right is None:
                node.right = BSTNode(data)
            else:
                self.insert(data, node.right)

    def is_empty(self):
        return self.root is None

    def preorder(self, node):
        if node:
            print("->", node.data, end=" ")
            self.preorder(node.left)
            self.preorder(node.right)

    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print("->", node.data, end=" ")
            self.inorder(node.right)

    def postorder(self, node):
        if node:
            self.postorder(node.left)
            self.postorder(node.right)
            print("->", node.data, end=" ")

    def traverse(self):
        if self.is_empty():
            print("This is an empty binary search tree.")
            return

        print("Preorder: ", end="")
        self.preorder(self.root)
        print("")
        print("Inorder: ", end="")
        self.inorder(self.root)
        print("")
        print("Postorder: ", end="")
        self.postorder(self.root)

def main():
    my_bst = BST()
    for _ in range(int(input())):
        my_bst.insert(int(input()))
    my_bst.traverse()

main()