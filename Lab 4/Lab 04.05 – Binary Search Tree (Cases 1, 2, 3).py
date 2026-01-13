"""Lab 04.05 – Binary Search Tree (Cases 1, 2, 3)"""
class BSTNode:
    def __init__(self, data: int=None):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, data, node=None):
        if self.is_empty():
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

    def delete(self, data):
        def _delete(node, data):
            if node is None:
                print("Delete Error, " + str(data) + " is not found in Binary Search Tree.")
                return None

            if data < node.data:
                node.left = _delete(node.left, data)
            elif data > node.data:
                node.right = _delete(node.right, data)
            else:
                if node.left is None and node.right is None:
                    return None
                elif node.left is None:
                    return node.right
                elif node.right is None:
                    return node.left
                else:
                    max_val = self.find_max(node.left)
                    node.data = max_val
                    node.left = _delete(node.left, max_val)
            return node
        self.root = _delete(self.root, data)

    def find_min(self, node=None):
        if self.is_empty():
            return None
        if node is None:
            node = self.root
        if node.left is None:
            return node.data
        return self.find_min(node.left)

    def find_max(self, node=None):
        if self.is_empty():
            return None
        if node is None:
            node = self.root
        if node.right is None:
            return node.data
        return self.find_max(node.right)

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
    while 1:
        text = input()
        if text == "Done":
            break
        condition, data = text.split(": ")
        if condition == "I":
            my_bst.insert(int(data))
        elif condition == "D":
            my_bst.delete(int(data))
        else:
            print("Invalid Condition")
    my_bst.traverse()

main()