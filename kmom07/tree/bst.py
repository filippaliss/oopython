# bst.py
from node import Node

class BinarySearchTree:
    def __init__(self):
        self.root = None
        self._size = 0

    def insert(self, key, value):
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
        self._inorder_recursive(self.root)

    def _inorder_recursive(self, node):
        if node is not None:
            self._inorder_recursive(node.left)
            print(node.value)
            self._inorder_recursive(node.right)

    def get(self, key):
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
        node = self._find(self.root, key)
        if node is None:
            raise KeyError(f"Key {key} not found in tree")
        self._size -= 1
        return self._remove_node(node)

    def _remove_node(self, node):
        if node.is_leaf():  # Inga barn
            self._replace_node_in_parent(node, None)
        elif node.has_both_children():  # Två barn
            successor = self._find_min(node.right)
            node.key, node.value = successor.key, successor.value
            return self._remove_node(successor)
        else:  # Ett barn
            child = node.left if node.has_left_child() else node.right
            self._replace_node_in_parent(node, child)
        return node.value

    def _replace_node_in_parent(self, node, new_node):
        if node.has_parent():
            if node.is_left_child():
                node.parent.left = new_node
            else:
                node.parent.right = new_node
        else:
            self.root = new_node
        if new_node is not None:
            new_node.parent = node.parent

    def _find_min(self, node):
        while node.has_left_child():
            node = node.left
        return node

    def size(self):
        return self._size
