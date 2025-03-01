"""
    UnorderedList filen, som implementerar en enkel oordnad lista med
    metoder för att lägga till, hämta och ta bort element.
"""
class UnorderedList:
    def __init__(self):
        self.items = []

    def add(self, value):
        """
        Lägger till ett värde i listan.
        """
        self.items.append(value)

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
