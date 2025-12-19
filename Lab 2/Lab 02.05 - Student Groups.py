"""Lab 02.05 - Student Groups"""
class ArrayStack:
    def __init__(self):
        self.size = 0
        self.data = []

    def push(self, input_data):
        """Stack"""
        try:
            if input_data.isdigit():
                input_data = int(input_data)
            elif input_data.replace(".", "", 1).isdigit():
                input_data = float(input_data)
        except (TypeError, ValueError, ArithmeticError, AttributeError):
            pass
        finally:
            self.data.append(input_data)
            self.size += 1

    def pop(self):
        """pop"""
        if self.size > 0:
            value =  self.data.pop()
            self.size -= 1
            return value
        else:
            print("Underflow: Cannot pop data from an empty list")
            return None

    def is_empty(self):
        """is_empty"""
        return not self.data

    def get_size(self):
        """get_size"""
        return self.size

    def get_stack_top(self):
        """get_stack_top"""
        if self.size > 0:
            return self.data[-1]
        else:
            print("Underflow: Cannot get stack top from an empty list")
            return None

    def print_stack(self):
        """print_stack"""
        print(self.data)

m = int(input())
n = int(input())
stack_name = ArrayStack()
for _ in range(n):
    name = input()
    stack_name.push(name)
# stack_name.print_stack()

group_list = [ArrayStack() for _ in range(m)]

for i in range(stack_name.get_size()):
    group = i % m
    name = stack_name.pop()
    group_list[group].push(name)

for i in range(len(group_list)):
    sum_name = ""
    for name in group_list[i].data:
        sum_name += f"{name}, "
    print(f"Group {i + 1}: {sum_name.rstrip(", ")}")
    
