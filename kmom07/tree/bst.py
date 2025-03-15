# bst.py
from node import Node
"""
BinarySearchTree lösningar
"""
class BinarySearchTree:
    """
    bst class
    """
    def __init__(self):
        self.root = None
        self._size = 0
    
    def size(self):
        return self._size
    def insert(self, key, value):
        def _insert(node, key, value, parent):
            if node is None:
                self._size += 1
                return Node(key, value, parent)
            if key < node.key:
                node.left = _insert(node.left, key, value, node)
            elif key > node.key:
                node.right = _insert(node.right, key, value, node)
            else:
                node.value = value
            return node
        
        self.root = _insert(self.root, key, value, None)

    def inorder_traversal_print(self):
        def _inorder(node):
            if node:
                _inorder(node.left)
                print(node.value)
                _inorder(node.right)
        _inorder(self.root)

    
    def get(self, key):
        def _get(node, key):
            if node is None:
                raise KeyError(f"Key {key} not found.")
            if key < node.key:
                return _get(node.left, key)
            elif key > node.key:
                return _get(node.right, key)
            else:
                return node.value

        return _get(self.root, key)

    
    def remove(self, key):
        def _remove(node, key):
            if node is None:
                raise KeyError(f"Key {key} not found.")
        
            if key < node.key:
                node.left = _remove(node.left, key)
            elif key > node.key:
                node.right = _remove(node.right, key)
            else:
                # Fall 1: Löv
                if node.left is None and node.right is None:
                    self._size -= 1
                    return None, node.key  # Returnerar nodens nyckel för att användas senare
                
                # Fall 2: Enbart vänster eller höger barn
                elif node.left is None:
                    self._size -= 1
                    return node.right, node.key
                elif node.right is None:
                    self._size -= 1
                    return node.left, node.key
                # Fall 3: Två barn
                else:
                    min_node = self._find_min(node.right)
                    node.key, node.value = min_node.key, min_node.value
                    node.right, _ = _remove(node.right, min_node.key)
                    return node, node.key

            return node, key

        self.root, removed_key = _remove(self.root, key)
        return str(removed_key) 

    def _find_min(self, node):
        while node.left:
            node = node.left
        return node

