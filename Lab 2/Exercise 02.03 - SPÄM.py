"""Exercise 02.03 - SPÄM"""
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
        # else:
        #     print("Underflow: Cannot get stack top from an empty list")
        #     return None

    def print_stack(self):
        """print_stack"""
        print(self.data)

def is_parentheses_matching(input_):
    sta = ArrayStack()
    not_OpenBracket = True
    for i in input_:
        if i in "({[":
            sta.push(i)
        elif i in ")}]":
            if (i == ")" and sta.get_stack_top() != "(") or (i == "}" and sta.get_stack_top() != "{") or (i == "]" and sta.get_stack_top() != "["):
                # print("Underflow: Cannot pop data from an empty list")
                sta.pop()
                not_OpenBracket = False
                return False
            sta.pop()
    return sta.is_empty() if not_OpenBracket else False

data = input()
result =  is_parentheses_matching(data)
print(result)
