class LinkedList:
    class Node:
        __slots__ = 'data', 'next'

        def __init__(self, data, next):
            self.data = data
            self.next = next

    def __init__(self):
        self.head = None  # assigning None to head and tail means initially the linked list is empty
        self.tail = None
        self.size = 0

    def __len__(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def add_first(self, data): # The method is use to insert item at the begining of the linked list
        newest = self.Node(data, None) # Create a newest node, then pass data and next as argument.
        if self.is_empty():
            self.head = newest
            self.tail = newest
        else: # This is the case when the linked list has some nodes
            newest.next = self.head # assign newest.next to the begining, i.e self.head
        self.head = newest # make head as the newest
        self.size += 1 # finally we increase the size of the linked list by 1

    def add_last(self, data): # to insert data at the end of the linked list
        newest =  self.Node(data, None)
        if self.is_empty(): # check if the list is empty
            self.head = newest # if yes self.head is assigned newest and tail will be assigned newest
            self.tail = newest
        else:  # if not empty then:
            self.tail.next = newest # we make self.tail.next as the newest
        self.tail = newest # shift the tail by using self.tail = newest
        self.size += 1

    def display(self): # this will help us to know the element that are present in the linked list
        thead = self.head # we assign self.head to thead, which means we are declaring a temporary head.
        while thead: # we will check while thead is not null, then we will print thead.data
            print(thead.data, end='-->')
            thead = thead.next
        print() # then finally use a print function to print a new line


    def add_any(self, data, position):
        if position == 1:
            self.add_first(data)
        elif position < 1:
            print("Invalid position")
        else:
            newest = self.Node(data, None)
            thead = self.head
            i = 2
            while i < position:
                thead = thead.next
                if thead.next is None:
                    break
                i += 1
            newest.next = thead.next
            thead.next = newest
            self.size += 1

    def del_any(self, position):
        if position == 1:
            self.head = self.head.next

        else:
            previous = None
            thead = self.head
            i = 1
            while i < position:
                previous = thead
                thead = thead.next
                i += 1
                # print(f"prev {previous.data}")
                # print(f"thead {thead.data}")
            previous.next = thead.next
        self.size -= 1




l = LinkedList()
l.add_last(10)
l.add_last(20)
l.add_last(30)
l.add_any(11, 2)
l.add_any(12, 2)
l.add_any(14, 4)
l.add_any(111, 14)
l.add_any(0, 1)
l.display()
l.del_any(3)
l.del_any(1)
l.display()
