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
        if self.head is None:
            self.head = new
            self.count += 1
            return
        new.next = self.head 
        self.head = new

    def insert_before(self, node, data):
        if self.head is None:
            print(f"Cannot insert, " + node + " does not exist.")
            return
        if self.head.data == node:
            self.insert_front(data)
            return
        new = DataNode(data)
        pre = self.head
        while pre.next and pre.next.data != node:
            pre = pre.next
        if pre.next is None:
            print("Cannot insert, " + node + " does not exist.")
            return
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
        pre.next = pre.next.next
        self.count -= 1
        

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

def append(list1, list2):
    if list2.head is None:
        return
    temp = list2.head
    while temp:
        list1.insert_last(temp.data)
        temp = temp.next
    print("1: ",end="")
    list1.traverse()
    print("2: ",end="")
    list2.traverse()

def condition_LinkedList(mylist):
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
        elif condition == "D":
            mylist.delete(data)
        else:
            print("Invalid Condition!")
    mylist.traverse()

def main():
    print("mylist1")
    mylist1 = SinglyLinkedList()
    condition_LinkedList(mylist1)

    print("\nmylist2")
    mylist2 = SinglyLinkedList()
    condition_LinkedList(mylist2)

    print("\nmylist3")
    mylist3 = SinglyLinkedList()
    condition_LinkedList(mylist3)    

    print("\nappend1")
    append(mylist1, mylist2)

    print("\nappend2")
    append(mylist1, mylist3)

    print("\nappend3")
    Temp = mylist1
    append(mylist1, Temp)
main()

# 5
# F: a
# L: b
# L: c
# F: d
# L: e
# 4
# L: Pubeth
# F: Teerapat
# F: Sonrasamon
# L: Siwapat
# 2
# L: HEE
# L: GG