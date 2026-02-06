class DataNode:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.count = 0
        self.head = None
    
    def insert_last(self, data):
        new = DataNode(data)
        if self.head is None:
            self.head = new
            self.count += 1
            return
        tra = self.head
        while tra.next:
            tra = tra.next
        tra.next = new
        self.count += 1

    def insert_front(self, data):
        new = DataNode(data)
        new.next = self.head
        self.head = new
        self.count += 1

    def insert_before(self, num, data):
        new = DataNode(data)
        if int(num) > self.count:
            print("เกิน")
            return
        if int(num) == 1:
            self.insert_front(data)
            return
        pre = self.head
        for _ in range(int(num) - 1):
            pre = pre.next
        new.next = pre.next
        pre.next = new
        self.count += 1

    def insert_lest_data(self, node, data):
        new = DataNode(data)
        if self.head is None:
            print("ไม่มี")
            return
        tra = self.head
        while tra and tra.data != node:
            tra = tra.next
        if tra is None:
            print("ไม่มี 2")
        new.next = tra.next
        tra.next = new
        self.count += 1
    
    def insert_lest_dataIndex(self, index, data):
        index = int(index)
        new = DataNode(data)
        if index > self.count:
            print("เกิน")
            return
        if index == 1:
            new.next = self.head.next
            self.head.next = new
            self.count += 1
            return
        pre = self.head
        for _ in range(index - 1):
            pre = pre.next
        new.next = pre.next
        pre.next = new
        self.count += 1

    def delete(self, data):
        if self.head is None:
            print("ไม่มี Node")
            return
        if self.head.data == data:
            self.head = self.head.next
            self.count -= 1
            return
        pre = self.head
        while pre.next and pre.next.data != data:
            pre = pre.next
        if pre.next is None:
            print("ไม่มี node")
            return
        pre.next = pre.next.next
        self.count -= 1

    def deleteIndex(self, index):
        index = int(index)
        if index > self.count:
            print("index เกิน")
            return
        if index == 1:
            self.head = self.head.next
            self.count -= 1
            return
        pre = self.head
        for _ in range(index - 2):
            pre = pre.next
        pre.next = pre.next.next
        self.count -= 1

    def traverse(self):
        result = ""
        tra = self.head
        while tra:
           result += tra.data + " => "
           tra = tra.next
        print(result.rstrip(" => "))


def main():
    mylist = SinglyLinkedList()
    for _ in range(int(input())):
        text = input()
        condition, data = text.split(": ")
        condition = condition.upper()
        if condition == "F":
            mylist.insert_front(data)
        elif condition == "L":
            mylist.insert_last(data)
        elif condition == "B":
            mylist.insert_before(*data.split(", "))
        elif condition == "I":
            mylist.deleteIndex(data)
        elif condition == "R":
            mylist.insert_lest_data(*data.split(", "))
        elif condition == "O":
            mylist.insert_lest_dataIndex(*data.split(", "))
        elif condition == "D":
            mylist.delete(data)
        else:
            print("Invalid Condition!")
        mylist.traverse()
main()

# 10
# F: A
# L: B
# L: D
# L: F
# B: 2, C
# B: 1, L
# D: A
# I: 3
# R: D, H
# O: 3, O
