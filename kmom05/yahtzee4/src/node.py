"""
Definierar en enkel nodklass för användning i länkade listor.
"""
class Node:
    """
    Representerar en nod i en länkad lista, som håller data och en referens till nästa nod.
    """
    def __init__(self, value):
        self.value = value
        self.next = None
