"""
klassen Queue gör så vi kan ha en kö som spelare går igenom
"""
class Queue:
    """queue är First In First Out"""
    def __init__(self):
        self._items = []

    def is_empty(self):
        """Returnerar True/False beroende på om kön är tom"""
        return not self._items

    def enqueue(self, item):
        """Lägger till"""
        self._items.append(item)

    def dequeue(self):
        """Tar bort"""
        try:
            return self._items.pop(0)

        except IndexError:
            return "Empty list."

    def peek(self):
        """Visar vad som ligger överst utan att ändra i kön"""
        return self._items[0]

    def size(self):
        """Returnerar antalet element i kön)"""
        return len(self._items)

    def to_list(self):
        """Returneraren lista av queue"""
        return self._items[:]
