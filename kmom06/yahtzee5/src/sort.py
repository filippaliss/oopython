"""
Skapa filen src/sort.py och kopiera in insertion sort från artikeln.
src/sort.py ska inte innehålla någon klass. Det räcker med enbart funktion för algoritmen.

Justera Insertion sort funktionen så den kan sortera din UnorderedList. PS! När ni skapar sorterings algoritmerna ska ni använda er av metoderna på Unorderdlist objektet för att flytta på element. Ni ska inte hämta head och traversera noder med den i era algoritmer eller gör om det till en inbyggd lista.

I src/sort.py skapa en rekursiv insertion sort algoritm som kan sortera din lista. Döp den till recursive_insertion.

Sorteringsalgoritmerna ska fungera oberoende av vilken data som sparas i UnorderedList. Algoritmerna ska inte ha någon kunskap om vilken data som finns listan.

Använd din rekursiva insertion sort för att sortera UnorderedList i topplista vyn. Sortera på antalet poäng.
"""

# def insertion_sort(items):
#     """ Insertion sort """
#     for i in range(1, len(items)):
#         j = i
#         while j > 0 and items[j] < items[j-1]:
#             items[j], items[j-1] = items[j-1], items[j]
#             j -= 1

#     return items

def recursive_insertion(unsorted_list, current_node):
    """
    Rekursiv insertion sort för UnorderedList.
    Den här funktionen sorterar listan genom att iterera genom den och införa varje nod på rätt plats i den sorterade delen av listan.
    """

    # Basfall: Om det inte finns några fler noder att sortera, stoppa rekursionen
    if current_node is None or current_node.next is None:
        return unsorted_list

    # Ta nästa nod för att sortera den
    next_node = current_node.next

    # Införa den aktuella noden på rätt plats i den sorterade listan
    unsorted_list.head = insert_in_sorted_list(unsorted_list.head, current_node)

    # Rekursivt sortera resten av listan
    return recursive_insertion(unsorted_list, next_node)

def insert_in_sorted_list(sorted_head, new_node):
    """
    Hjälpfunktion för att sätta in en nod i en redan sorterad lista.
    Denna funktion säkerställer att vi håller listan sorterad.
    """
    
    # Om listan är tom eller om den nya nodens score är större än den första nodens score
    if sorted_head is None or new_node.data.score > sorted_head.data.score:
        new_node.next = sorted_head
        return new_node

    # Annars, gå igenom listan för att hitta rätt plats
    current = sorted_head
    while current.next is not None and current.next.data.score >= new_node.data.score:
        current = current.next

    # Sätt in den nya noden på rätt plats
    new_node.next = current.next
    current.next = new_node

    return sorted_head