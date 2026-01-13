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
            result += str(tra.data) + " -> "
            tra = tra.next
        print(result.rstrip(" -> "))

    def insert_last(self, data):
        if data is None:
            return
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
        if data is None:
            return
        new = DataNode(data)
        new.next = self.head
        self.head = new
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

    def delete_last(self):
        if self.head is None:
            return None
        if self.head.next is None:
            data = self.head.data
            self.head = None
            self.count -= 1
            return data
        pre = self.head
        while pre.next.next:
            pre = pre.next
        data = pre.next.data
        pre.next = None
        self.count -= 1
        return data

    def delete_front(self):
        if self.head is None:
            return None
        data = self.head.data
        self.head = self.head.next
        self.count -= 1
        return data

def main():
    n = int(input())
    node = SinglyLinkedList()
    for _ in range(n):  
        new = input()
        node.insert_last(new)

    result = SinglyLinkedList()
    f_node = True
    while node.count > 0:
        if f_node:
            result.insert_last(node.delete_last())
            f_node = False

        for _ in range(2):
            result.insert_last(node.delete_front())

        for _ in range(2):
            result.insert_last(node.delete_last())
    result.traverse()
main()
