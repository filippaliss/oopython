"""
sort funktionen i yatzee spelet
"""

def insertion_sort(unordered_list):
    """
    Insertion sort för UnorderedList
    """
    n = unordered_list.size()

    for i in range(1, n):
        j = i
        current_item = unordered_list.get(j)
        while j > 0 and unordered_list.get(j - 1) > current_item:
            unordered_list.set(j, unordered_list.get(j - 1))
            j -= 1

        unordered_list.set(j, current_item)

    return unordered_list

def recursive_insertion(unordered_list, index=1):
    """
    Rekursiv insertion sort för UnorderedList med antingen int eller str.
    """
    if index >= unordered_list.size():
        return unordered_list

    current_item = unordered_list.get(index)
    j = index

    if isinstance(current_item, tuple):
        while j > 0 and unordered_list.get(j - 1)[1] > current_item[1]:
            unordered_list.set(j, unordered_list.get(j - 1))
            j -= 1
    else:
        while j > 0 and unordered_list.get(j - 1) > current_item:
            unordered_list.set(j, unordered_list.get(j - 1))
            j -= 1

    unordered_list.set(j, current_item)

    return recursive_insertion(unordered_list, index + 1)
