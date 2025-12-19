"""Exercise 02.01 – Infix to Postfix V.1"""
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

def infixToPostfix(expression):
    stack = ArrayStack()
    postfix = ArrayStack()

    for i in expression:
        if i.isalpha():
            postfix.push(i)
        elif i in ("+-*/"):
            while (not stack.is_empty() and((i in "+-" and stack.get_stack_top() in "+-*/") or (i in "*/" and stack.get_stack_top() in "*/"))):
                n = stack.pop()
                postfix.push(n)  
            stack.push(i)
        elif i == "(":
            stack.push(i)
        elif i == ")":
            while stack.get_stack_top() != "(":
                n = stack.pop()
                postfix.push(n)
            stack.pop()

        # stack.print_stack()
        # postfix.print_stack()

    while not stack.is_empty():
        val = stack.pop()
        postfix.push(val)

    result = ""
    for val in postfix.data:
        result += f"{val}"
    return result


exp = input()
print(infixToPostfix(exp))
