"""Lab 06.03 - Binary Search"""
class Student:
    def __init__(self, std_id: int, name: str, gpa: float):
        self.std_id = std_id
        self.name = name
        self.gpa = gpa

    def get_std_id(self):
        return self.std_id

    def get_name(self):
        return self.name
        
    def get_gpa(self):
        return f"{self.gpa:.2f}"

    def print_details(self):
        print(f"ID: {self.get_std_id()}")
        print(f"Name: {self.get_name()}")
        print(f"GPA: {self.get_gpa()}")

def Binary_Search(data: list, name: str):
    count = 0
    begie = 0
    end = len(data) - 1

    while (begie <= end):
        count += 1
        mid = (begie + end) // 2
        if data[mid].get_name() == name:
            print(f"Found {name} at index {mid}")
            data[mid].print_details()
            print(f"Comparisons times: {count}")
            return
        if data[mid].get_name() < name:
            begie = mid + 1
        else:
            end = mid - 1
    print(f"{name} does not exists.")
    print(f"Comparisons times: {count}")

def main():
    import json
    input_std = json.loads(input())
    search_name = input()
    std_list = []
    for item in input_std:
        std_list.append(Student(item["id"], item["name"], item["gpa"]))
    Binary_Search(std_list, search_name)
main()