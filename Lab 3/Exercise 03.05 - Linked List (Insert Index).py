"""Exercise 03.05 - Linked List (Insert Index)"""
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
        if tra is None: 
            print("This is an empty list.")
            return
        while tra:
            result += tra.data + " "
            tra = tra.next
        print(result.rstrip(" "))

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

    def insert_before(self, index, data):
        new = DataNode(data)
        if index == 0:
            new.next = self.head
            self.head = new
            self.count += 1
            return
        pre = self.head
        for _ in range(index - 1):
            pre = pre.next
        new.next = pre.next
        pre.next = new
        self.count += 1

def main():
    n = int(input())
    mylist = SinglyLinkedList()
    for _ in range(n):
        mylist.insert_last(input())
    index = int(input())
    new_node = input()
    mylist.insert_before(index, new_node)
    mylist.traverse()
main()