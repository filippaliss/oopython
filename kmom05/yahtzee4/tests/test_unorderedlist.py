"""
Module to define unit tests for the UnorderedList class.
"""
import unittest
from src.unorderedlist import UnorderedList
from src.errors import MissingIndex, MissingValue

class TestUnorderedList(unittest.TestCase):
    """
    A test suite for the UnorderedList class.
    """
    def setUp(self):
        """
        Skapar en ny instans av UnorderedList innan varje test.
        """
        self.ulist = UnorderedList()

    def test_get_invalid_index(self):
        """
        Testar att ett MissingIndex-exception kastas om indexet inte finns.
        """
        with self.assertRaises(MissingIndex):
            self.ulist.get(0)

    def test_get_valid_index(self):
        """
        Testar att rätt värde returneras om index finns.
        """
        self.ulist.add(10)
        self.ulist.add(20)
        self.assertEqual(self.ulist.get(0), 10)
        self.assertEqual(self.ulist.get(1), 20)

    def test_remove_missing_value(self):
        """
        Testar att ett MissingValue-exception kastas om värdet saknas.
        """
        with self.assertRaises(MissingValue):
            self.ulist.remove(10)

    def test_remove_existing_value(self):
        """
        Testar att listan är korrekt efter att ett element har tagits bort.
        """
        self.ulist.add(10)
        self.ulist.add(20)
        self.ulist.add(30)
        self.ulist.remove(20)

        elements = []
        current = self.ulist.head
        while current:
            elements.append(current.value)
            current = current.next

        self.assertNotIn(20, elements)
        self.assertEqual(elements, [10, 30])

if __name__ == "__main__":
    unittest.main()
