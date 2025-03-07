from src.unorderedlist import UnorderedList

def insertion_sort(items):
    """ Insertion sort """
    for i in range(1, len(items)):
        j = i
        while j > 0 and items[j] < items[j-1]:
            items[j], items[j-1] = items[j-1], items[j]
            j -= 1

    return items


def recursive_insertion(unordered_list, index=1):
    if index >= unordered_list.size():
        return

    current_item = unordered_list.get(index)

    j = index
    while j > 0 and unordered_list.get(j - 1)[1] > current_item[1]:
        unordered_list.set(j, unordered_list.get(j - 1))
        j -= 1

    unordered_list.set(j, current_item)

    recursive_insertion(unordered_list, index + 1)


    return unordered_list
