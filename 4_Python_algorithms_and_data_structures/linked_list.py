class LinkedList:
    class Node:
        __slots__ = 'data', 'next'

        def __init__(self, data, next_element):
            self.data = data
            self.next = next_element

    def __init__(self):
        self.head = None  # assigning None to head and tail means initially the linked list is empty
        self.tail = None
        self.size = 0

    def __len__(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def add_first(self, data):  # The method is used to insert item at the beginning of the linked list
        newest = self.Node(data, None)  # Create the newest node, then pass data and next as argument.
        if self.is_empty():
            self.head = newest
            self.tail = newest
        else:  # This is the case when the linked list has some nodes
            newest.next = self.head  # assign newest.next to the beginning, i.e. self.head
        self.head = newest  # make head as the newest
        self.size += 1  # finally we increase the size of the linked list by 1

    def add_last(self, data):  # to insert data at the end of the linked list
        newest = self.Node(data, None)
        if self.is_empty():  # check if the list is empty
            self.head = newest  # if yes self.head is assigned newest and tail will be assigned newest
            self.tail = newest
        else:  # if not empty then:
            self.tail.next = newest  # we make self.tail.next as the newest
        self.tail = newest  # shift the tail by using self.tail = newest
        self.size += 1

    def display(self):  # this will help us to know the element that are present in the linked list
        t_head = self.head  # we assign self.head to t_head, which means we are declaring a temporary head.
        while t_head:  # we will check while t_head is not null, then we will print t_head.data
            print(t_head.data, end='-->')
            t_head = t_head.next
        print()  # then finally use a print function to print a new line

    def add_any(self, data, position):
        if position == 1:
            self.add_first(data)
        elif position < 1:
            print("Invalid position")
        else:
            newest = self.Node(data, None)
            t_head = self.head
            i = 2
            while i < position:
                t_head = t_head.next
                if t_head.next is None:
                    break
                i += 1
            newest.next = t_head.next
            t_head.next = newest
            self.size += 1

    def del_any(self, position):
        if position == 1:
            self.head = self.head.next

        else:
            previous = None
            t_head = self.head
            i = 1
            while i < position:
                previous = t_head
                t_head = t_head.next
                i += 1
                # print(f"prev {previous.data}")
                # print(f"t_head {t_head.data}")
            previous.next = t_head.next
        self.size -= 1


ll = LinkedList()
ll.add_last(10)
ll.add_last(20)
ll.add_last(30)
ll.add_any(11, 2)
ll.add_any(12, 2)
ll.add_any(14, 4)
ll.add_any(111, 14)
ll.add_any(0, 1)
ll.display()
ll.del_any(3)
ll.del_any(1)
ll.display()
