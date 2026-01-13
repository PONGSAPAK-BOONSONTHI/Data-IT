"""Exercise 03.03 - AlmostMean"""
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
        l = self.head
        while l.next:
            l = l.next
        l.next = new
        self.count += 1

def main():
    n = int(input())
    sum_score = 0
    id_link = SinglyLinkedList()
    for _ in range(n):
        input_ = input()
        _, score = input_.split(None)
        sum_score += float(score)
        id_link.insert_last(input_)
    ave = sum_score / id_link.count

    max_score = 0
    node = id_link.head
    result = ""
    while node:
        _, score = node.data.split()
        score = float(score)
        if score <= ave:
            if max_score < score:
                max_score = score
                result = node.data
        node = node.next
    print(result)
main()
