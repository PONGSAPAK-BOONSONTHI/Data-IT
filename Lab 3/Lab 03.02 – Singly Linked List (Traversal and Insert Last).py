"""Lab 03.02 – Singly Linked List (Traversal and Insert Last)"""
class DataNode:
  def __init__(self, data=None):
    self.data = data
    self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.count = 0
        self.head = None

    def traverse(self):
        result = ""
        tra = self.head
        if tra == None:
            print("This is an empty list.")
            return
        while tra:
            result += tra.data + " -> "
            tra = tra.next
        print(result.rstrip(" -> "))
    def insert_last(self, data):
        new = DataNode(data)
        if self.head is None:
            self.head = new
            self.count += 1
            return
        l = self.head
        while l.next:
            l = l.next
        l.next = new
        self.count += 1

def main():
    mylist = SinglyLinkedList()
    for _ in range(int(input())):
        mylist.insert_last(input().strip())
    mylist.traverse()
main()
