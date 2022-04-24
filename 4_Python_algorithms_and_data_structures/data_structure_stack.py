from dataclasses import dataclass


@dataclass(eq=True, order=True)
class Stack():
    def __init__(self, input_list=None):
        if input_list is None:
            self.__list = []
        else:
            self.__list = input_list

    def push(self, element) -> None:
        self.__list.append(element)
        print(f"Added {element} to stack")

    def pull(self):
        try:
            element = self.__list.pop(-1)
            print(f"Removed {element} from stack")
            return element

        except IndexError:
            print("Stack is empty")
            return None

    def is_empty(self) -> bool:
        return self.__list == []

    def length(self) -> int:
        return len(self.__list)

    def print(self) -> None:
        print(f"Elements in stack: {self.__list}")

    def __add__(self, other):
        return Stack(self.__list + other.__list)

    def __len__(self):
        return len(self.__list)


if __name__ == "__main__":
    stack1 = Stack()
    stack1.push(10)
    stack1.push("32")
    stack1.push("34")

    stack1.pull()

    stack2 = Stack([321, "adf"])

    stack3 = stack1 + stack2
    stack3.print()

    print(stack1 < stack3)
    print(stack1 <= stack2)
