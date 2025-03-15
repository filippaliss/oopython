"""
Node klassen 
"""
class Node:
    """
    En nod i ett binärt träd som lagrar en nyckel och ett värde
    samt referenser till sina barn- och föräldranoder.
    """
    def __init__(self, key, value, parent=None):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.parent = parent

    def has_left_child(self):
        """
        returnera True om noden har en left child nod, annars False.
        """
        return self.left is not None

    def has_right_child(self):
        """
        returnera True om noden har en right child nod, annars False.
        """
        return self.right is not None

    def has_both_children(self):
        """
        returnera True om noden har en left och en right child nod, annars False.
        """
        return self.has_left_child() and self.has_right_child()

    def has_parent(self):
        """
        returnera True om noden har en parent nod, annars False.
        """
        return self.parent is not None

    def is_left_child(self):
        """
        returnera True om noden är left child till sin parent nod, annars False.
        """
        return self.has_parent() and self.parent.left == self

    def is_right_child(self):
        """
        returnera True om noden är right child tills sin parent nod, annars False.
        """
        return self.has_parent() and self.parent.right == self

    def is_leaf(self):
        """ 
        returnera True om noden inte har några children noder (left eller right), annars False.
        """
        return not self.has_left_child() and not self.has_right_child()

    def __it__(self, other):
        """
        returnera True om nodens key är mindre än other, annars False.
        """
        return self.key < other.key

    def __gt__(self, other):
        """
        returnera True om nodens key är större än other, annars False.
        """
        return self.key > other.key

    def __eq__(self, other):
        """
        returnera True om nodens key är lika med other, annars False.
        """
        return self.key == other.key
