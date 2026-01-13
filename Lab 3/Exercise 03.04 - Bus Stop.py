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

    def delete(self, data):
        data = str(data)
        if self.head is None:
            # print(f"Cannot delete, " + data + " does not exist.")
            return False
        if self.head.data == data:
            self.head = self.head.next
            self.count -= 1
            return True
        pre = self.head
        while pre.next and pre.next.data != data:
            pre = pre.next
        if pre.next is None:
            # print(f"Cannot delete, " + data + " does not exist.")
            return False
        sta = pre.next
        pre.next = sta.next
        del sta
        self.count -= 1
        return True

def main():
    bus = SinglyLinkedList()
    p = int(input())
    n = int(input())
    re_count = 0
    
    for _ in range(n):
        stop_num, pas_gers = input().split(" ", 1)
        pas_gers = pas_gers.split()
        while bus.delete(stop_num):
            re_count += 1
        for i in pas_gers:
            dest_stop = int(i)
            if bus.count < p and dest_stop > int(stop_num):
                bus.insert_last(i)
        bus.traverse()
    print(re_count)
main()
