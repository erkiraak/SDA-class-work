from abc import ABC, abstractmethod

"""
Target interface - class ClientInterface
"""


class ClientInterface(ABC):
    @abstractmethod
    def push(self, data):
        pass

    @abstractmethod
    def pop(self):
        pass

    @abstractmethod
    def is_empty(self):
        pass


"""
The old class which we want to adapt
Reverse Polish Notation Parser - www.101computing.net/reverse-polish-notation/
"""

class Stack:
    def __init__(self):
        self.items = []
        # print("Stack created")

    def append(self, items):
        # print("appended with stack")
        self.items.append(items)

    def pop(self):
        # print("popped with stack")
        return self.items.pop()

    def len(self):
        return self.items.__len__()


class StackAdapterObject(ClientInterface):
    def __init__(self, stack):
        self._stack = stack

    def push(self, data):
        self._stack.append(data)

    def pop(self):
        return self._stack.pop()

    def is_empty(self):
        return self._stack.len() == 0


class StackAdapterClass(ClientInterface, Stack):
    def __init__(self):
        super().__init__()

    def push(self, data):
        self.append(data)

    def pop(self):
        return Stack.pop(self)

    def is_empty(self):
        return self.len() == 0




# Perform a basic arithmetic operation using +,-,*,/,^
def calculate(operator, operand1, operand2):
    if operator == "+":
        return operand1 + operand2
    elif operator == "-":
        return operand1 - operand2
    elif operator == "*":
        return operand1 * operand2
    elif operator == "/":
        return operand1 / operand2
    elif operator == "^":  # exponentiation operator
        return operand1 ** operand2

    # Evaluate an RPN expression


def postfixEval(expression, type_of_stack_adapter):
    operators = ["+", "-", "*", "/", "^"]
    if type_of_stack_adapter == "object":
        stack_adapter = StackAdapterObject(Stack())
    elif type_of_stack_adapter == "class":
        stack_adapter = StackAdapterClass()
    tokenList = expression.split(" ")

    for token in tokenList:
        # Check is the token is an operator or an operand!
        if token in operators:
            operand2 = stack_adapter.pop()
            operand1 = stack_adapter.pop()
            result = calculate(token, operand1, operand2)
            stack_adapter.push(result)
        else:  # Toke is an Operand
            stack_adapter.push(float(token))

    return stack_adapter.pop()
if __name__ == "__main__":
    ########################################################
    print(" ### Reverse Polish Notation Parser ###")
    expression = "2 7 + 3 / 14 3 - 4 * + 2 /"
    print("Expression 1:")
    print(expression)
    print(f"result with adapter object: {postfixEval(expression, 'object')}")
    print(f"result with adapter class: {postfixEval(expression, 'class')}")
    print("\n")
    print("Expression 2:")
    expression = "12 2 3 4 * 10 5 / + * +"
    print(expression)
    print(f"result with adapter object: {postfixEval(expression, 'object')}")
    print(f"result with adapter class: {postfixEval(expression, 'class')}")
    print("\n")
    print("Expression 3:")
    expression = "5 1 2 + 4 * + 3 -"
    print(expression)
    print(f"result with adapter object: {postfixEval(expression, 'object')}")
    print(f"result with adapter class: {postfixEval(expression, 'class')}")
