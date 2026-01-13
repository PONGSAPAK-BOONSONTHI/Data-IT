"""Lab 04.02 - Binary Search Tree (Preorder, Insert)"""
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

    def preorder(self, node):
        if node:
            print("->", node.data, end=" ")
            self.preorder(node.left)
            self.preorder(node.right)
def main():
    my_bst = BST()
    for _ in range(int(input())):
        my_bst.insert(int(input()))
        
    print("Preorder: ", end="")
    my_bst.preorder(my_bst.root)

main()