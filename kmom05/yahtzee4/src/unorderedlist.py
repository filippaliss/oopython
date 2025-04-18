"""
    UnorderedList filen, som implementerar en enkel oordnad lista med
    metoder för att lägga till, hämta och ta bort element.
"""
from src.errors import MissingIndex, MissingValue
from src.node import Node



class UnorderedList:
    """
    A class representing the UnorderedList using a linked list.
    """
    def __init__(self):
        self.head = None
        self._size = 0

    def append(self, value):
        """
        Adds a value to the end of the list.
        """
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        self._size += 1

    def add(self, value):
        """
        Alias for append.
        """
        self.append(value)

    def get(self, index):
        """
        Gets the value at the specified index.
        """
        if index < 0 or index >= self._size:
            raise MissingIndex("Index out of bounds.")
        current = self.head
        for _ in range(index):
            current = current.next
        return current.value

    def remove(self, value):
        """
        Removes a value from the list if present.
        """
        current = self.head
        previous = None

        while current:
            if current.value == value:
                if previous:
                    previous.next = current.next
                else:
                    self.head = current.next
                self._size -= 1
                return
            previous = current
            current = current.next

        raise MissingValue("Value not found.")

    def size(self):
        """
        Returns the number of items in the list.
        """
        return self._size

    def index_of(self, value):
        """
        Returns the index of the given value in the list.
        Raises MissingValue if the value is not found.
        """
        current = self.head
        index = 0
        while current:
            if current.value == value:
                return index
            current = current.next
            index += 1
        raise MissingValue("Value not found.")

    def print_list(self):
        """
        Prints all elements in the list.
        """
        elements = []
        current = self.head
        while current:
            elements.append(current.value)
            current = current.next
        print(elements)

    def set(self, index, value):
        """
        Sets the value at the given index in the list.
        Raises MissingIndex if the index is out of bounds.
        """
        if index < 0 or index >= self._size:
            raise MissingIndex("Index out of bounds.")
        current = self.head
        for _ in range(index):
            current = current.next
        current.value = value
    def __iter__(self):
        """
        returnerar en iterator över en kopierad lista.
        """
        elements = []
        current = self.head
        while current:
            elements.append(current.value)
            current = current.next
        return iter(elements)
