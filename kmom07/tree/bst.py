"""
BinarySearchTree klassen 
"""
from node import Node
class BinarySearchTree:
    """
    En klass som representerar ett binärt sökträd (BST) med
    funktioner för insättning, borttagning, sökning och inorder-traversering.
    """
    def __init__(self):
        self.root = None
        self._size = 0

    def size(self):
        """
        Returnera antalet noder i trädet. 
        Skapa denna tidigt, testerna använde den.
        """
        return self._size

    def insert(self, key, value):
        """
        Skapar en ny nod med key och value.
        Lägger till en noden på rätt plats i trädet, baserat på key.
        Om nod med key redan finns i trädet skriv över värdet i noden.
        """
        if self.root is None:
            self.root = Node(key, value)
        else:
            self._insert_recursive(self.root, key, value)
        self._size += 1

    def _insert_recursive(self, current, key, value):
        if key < current.key:
            if current.left is None:
                current.left = Node(key, value)
                current.left.parent = current
            else:
                self._insert_recursive(current.left, key, value)
        elif key > current.key:
            if current.right is None:
                current.right = Node(key, value)
                current.right.parent = current
            else:
                self._insert_recursive(current.right, key, value)
        else:
            current.value = value  # Skriv över värdet om nyckeln redan finns
            self._size -= 1  # Undvik att storleken ökar om vi bara skriver över

    def inorder_traversal_print(self):
        """
        Skriver ut värdet i noderna i trädet i rätt ordning,
        lågt till högt. En rad per värde.
        """
        self._inorder_recursive(self.root)

    def _inorder_recursive(self, node):
        if node is not None:
            self._inorder_recursive(node.left)
            print(node.value)
            self._inorder_recursive(node.right)

    def get(self, key):
        """
        Returnera value från noden med nyckeln key.
        Om key inte finns i trädet lyft ett KeyError exception (det inbyggda).
        """
        node = self._find(self.root, key)
        if node is None:
            raise KeyError(f"Key {key} not found in tree")
        return node.value

    def _find(self, node, key):
        if node is None or node.key == key:
            return node
        if key < node.key:
            return self._find(node.left, key)
        return self._find(node.right, key)

    def remove(self, key):
        """
        Ta bort nod med samma key, returnera värdet från noden.
        Om nod med key inte finns lyft KeyError exception (det inbyggda).
        """
        node = self._find(self.root, key)
        if node is None:
            raise KeyError(f"Key {key} not found in tree")
        self._size -= 1
        return self._remove_node(node)

    def _remove_node(self, node):
        original_value = node.value  # Spara det ursprungliga värdet

        if node.is_leaf():  # Inga barn
            self._replace_node_in_parent(node, None)

        elif node.has_both_children():  # Två barn
            successor = self._find_min(node.right)
            node.key, node.value = successor.key, successor.value
            self._remove_node(successor)  # Ta bort successorn från dess ursprungliga plats

        else:  # Endast ett barn
            child = node.left if node.has_left_child() else node.right
            self._replace_node_in_parent(node, child)

        return original_value

    def _replace_node_in_parent(self, node, new_node):
        if node.parent is not None:  # Kontrollera att noden har en parent
            if node.is_left_child():
                node.parent.left = new_node
            elif node.is_right_child():
                node.parent.right = new_node

        else:  # Om noden är root
            self.root = new_node

        if new_node is not None:
            new_node.parent = node.parent  # Uppdatera föräldern till den nya noden

    def _find_min(self, node):
        while node.has_left_child():
            node = node.left
        return node
