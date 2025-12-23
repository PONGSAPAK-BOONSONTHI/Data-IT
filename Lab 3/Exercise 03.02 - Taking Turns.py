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

def main():
    n = int(input())
    node = SinglyLinkedList()
    for _ in range(n):
        new = input()
main()
