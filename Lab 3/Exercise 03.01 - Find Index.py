"""Exercise 03.01 - Find Index"""
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

    def insert_front(self, data):
        new = DataNode(data)
        new.next = self.head
        self.head = new
        self.count += 1

    def insert_before(self, node, data):
        if self.head is None:
            print(f"Cannot insert, " + node + " does not exist.")
            return
        if self.head.data == node:
            self.insert_front(data)
            return
        pre = self.head
        while pre.next and pre.next.data != node:
            pre = pre.next
        if pre.next is None:
            print("Cannot insert, " + node + " does not exist.")
            return
        new = DataNode(data)
        new.next = pre.next
        pre.next = new
        self.count += 1

    def delete(self, data):
        if self.head is None:
            print(f"Cannot delete, " + data + " does not exist.")
            return
        if self.head.data == data:
            self.head = self.head.next
            self.count -= 1
            return
        pre = self.head
        while pre.next and pre.next.data != data:
            pre = pre.next
        if pre.next is None:
            print(f"Cannot delete, " + data + " does not exist.")
            return
        sta = pre.next
        pre.next = sta.next
        del sta
        self.count -= 1

    def search(self, num):
        if self.count < num or num <= 0:
            print("Error")
            return
        pre = self.head
        for _ in range(num - 1):
            pre = pre.next
        print(pre.data)

def main():
    Node = SinglyLinkedList()
    while True:
        new_node = input()
        if new_node == "Last":
            break
        Node.insert_last(new_node)
    n_node = int(input())
    Node.search(n_node)
main()