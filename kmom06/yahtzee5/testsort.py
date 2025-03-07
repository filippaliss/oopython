from src.unorderedlist import UnorderedList
from src.sort import recursive_insertion

# Exempel på test
unordered_list = UnorderedList()
unordered_list.add(("Alice", 200))
unordered_list.add(("Bob", 100))
unordered_list.add(("Charlie", 300))

# Skriv ut listan före sortering
print("Före sortering:")
unordered_list.print_list()

# Sortera listan
recursive_insertion(unordered_list)

# Skriv ut listan efter sortering
print("Efter sortering:")
unordered_list.print_list()
