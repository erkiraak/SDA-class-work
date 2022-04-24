from dataclasses import dataclass


@dataclass(eq=True, order=True)
class Queue:
    def __init__(self, input_list=None):
        if input_list is None:
            self.__list = []
        else:
            self.__list = input_list

    def push(self, element) -> None:
        self.__list.insert(0, element)
        print(f"Added {element} to queue")

    def pull(self):
        try:
            element = self.__list[-1]
            self.__list = self.__list[:-1]
            print(f"Removed {element} from queue")
            return element

        except IndexError:
            print("Queue is empty")
            return None

    def is_empty(self) -> bool:
        return self.__list == []

    def length(self) -> int:
        return len(self.__list)

    def print(self) -> None:
        print(f"Elements in queue: {self.__list}")

    def __add__(self, other):
        return Queue(self.__list + other.__list)

    def __len__(self):
        return len(self.__list)


if __name__ == "__main__":
    q1 = Queue()
    q1.push(10)
    q1.push("32")
    q1.push("34")

    q1.pull()
    q1.push("32")

    q2 = Queue([321, "adf"])

    q3 = q1 + q2
    q3.print()

    print(q1 < q3)
    print(q1 <= q2)
