"""
    UnorderedList filen, som implementerar en enkel oordnad lista med
    metoder för att lägga till, hämta och ta bort element.
"""
from src.errors import MissingIndex, MissingValue

class Node:
    def __init__(self, name, score):
        self.name = name  # Lagra namn
        self.score = score  # Lagra poäng
        self.next = None  # Nästa nod, initialiseras som None


class UnorderedList:
    """
    A class representing the UnorderedList.
    """
    def __init__(self):
        self.head = None

    def append(self, name, score):
        """Lägger till en ny spelare i listan."""
        new_node = Node(name, score)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def add(self, value):
        """
        Lägger till ett värde i listan. (Same functionality as append)
        """
        self.append(value)

    def get(self, index):
        """
        Hämtar värdet på den angivna indexpositionen i listan.
        """
        if index < 0 or index >= len(self.items):
            raise MissingIndex("Index out of bounds.")
        return self.items[index]

    def remove(self, value):
        """
        Tar bort ett värde från listan om det finns.
        """
        if value not in self.items:
            raise MissingValue("Value not found.")
        self.items.remove(value)

    def size(self):
        """
        Return the number of items in the list.
        """
        return len(self.items)

    def index_of(self, value):
        """
        Returns the index of the given value in the list.
        Raises MissingValue if the value is not found.
        """
        if value not in self.items:
            raise MissingValue("Value not found.")
        return self.items.index(value)

    def print_list(self):
        """
        Skriver ut hela listan.
        """
        current = self.head
        while current:
            print(f"{current.data[0]}: {current.data[1]}")
            current = current.next

    def to_list(self):
        """Konverterar länkade listan till en vanlig lista (för att spara till fil)."""
        result = []
        current = self.head
        while current:
            result.append(current.data)
            current = current.next
        return result

    def set(self, index, value):
        """
        Sets the value at the given index in the list.
        Raises MissingIndex if the index is out of bounds.
        """
        if index < 0 or index >= len(self.items):
            raise MissingIndex("Index out of bounds.")
        self.items[index] = value
