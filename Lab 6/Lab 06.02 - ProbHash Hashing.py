"""Lab 06.02 - ProbHash Hashing"""
class Student:
    def __init__(self, std_id: int, name: str, gpa: float):
        self.std_id = std_id
        self.name = name
        self.gpa = gpa

    def get_std_id(self) -> int:
        return self.std_id

    def get_name(self) -> str:
        return self.name
        
    def get_gpa(self) -> float:
        return f"{self.gpa:.2f}"

    def print_details(self):
        print(f"ID: {self.get_std_id()}")
        print(f"Name: {self.get_name()}")
        print(f"GPA: {self.get_gpa()}")

class ProbHash:
    def __init__(self, size: int):
        self.hash_table = [None] * size
        self.size = size
    
    def hash(self, key: int) -> int:
        return key % self.size

    def rehash(self, hkey: int) -> int:
        return (hkey + 1) % self.size

    def insert_data(self, std: Student) -> None:
        index = self.hash(std.get_std_id())
        start_index = index

        while self.hash_table[index] is not None:
            index = self.rehash(index)
            if index == start_index:
                print(f"The list is full. {std.get_std_id()} could not be inserted.")
                return
        self.hash_table[index] = std
        print(f"Insert {self.hash_table[index].get_std_id()} at index {index}")

    def search_data(self, std_id: int) -> Student:
        index = self.hash(std_id)
        start_index = index

        while self.hash_table[index] is not None:
            if self.hash_table[index].get_std_id() == std_id:
                print(f"Found {std_id} at index {index}")
                return self.hash_table[index]
            index = self.rehash(index)
            if index == start_index:
                break
        return print(f"{std_id} does not exist.")

def main():
    import json
    size = int(input())
    hashtable = ProbHash(size)
    while True:
        finish = input()
        if finish == "Done":
            break
        condition, data = finish.split(" = ")
        if condition == "I":
            std_in = json.loads(data)
            std = Student(std_in["ID"], std_in["Name"], std_in["GPA"])
            hashtable.insert_data(std)
        elif condition == "S":
            print("------")
            student = hashtable.search_data(int(data))
            if student is not None:
                student.print_details()
            print("------")
        else:
            print("Invalid Condition!")
main()