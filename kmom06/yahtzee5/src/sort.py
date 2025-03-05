"""
Skapa filen src/sort.py och kopiera in insertion sort från artikeln.
src/sort.py ska inte innehålla någon klass. Det räcker med enbart funktion för algoritmen.

Justera Insertion sort funktionen så den kan sortera din UnorderedList. PS! När ni skapar sorterings algoritmerna ska ni använda er av metoderna på Unorderdlist objektet för att flytta på element. Ni ska inte hämta head och traversera noder med den i era algoritmer eller gör om det till en inbyggd lista.

I src/sort.py skapa en rekursiv insertion sort algoritm som kan sortera din lista. Döp den till recursive_insertion.

Sorteringsalgoritmerna ska fungera oberoende av vilken data som sparas i UnorderedList. Algoritmerna ska inte ha någon kunskap om vilken data som finns listan.

Använd din rekursiva insertion sort för att sortera UnorderedList i topplista vyn. Sortera på antalet poäng.
"""

def insertion_sort(items):
    """ Insertion sort """
    for i in range(1, len(items)):
        j = i
        while j > 0 and items[j] < items[j-1]:
            items[j], items[j-1] = items[j-1], items[j]
            j -= 1

    return items

def recursive_insertion(ulist):
    """ Rekursiv insertion sort för UnorderedList """
    if ulist.size() <= 1:
        return  # Basfall: om listan är tom eller har ett element är den redan sorterad

    # Ta bort det första elementet
    first = ulist.get(0)
    ulist.remove(first)

    # Sortera resten av listan rekursivt
    recursive_insertion(ulist)

    # Sätt in det borttagna elementet på rätt plats i den sorterade listan
    insert_sorted(ulist, first)

def insert_sorted(ulist, value):
    """ Hjälpfunktion för att sätta in ett värde på rätt plats i en sorterad lista """
    # Vi går igenom listan och letar efter den rätta positionen
    position = 0
    while position < ulist.size() and ulist.get(position) > value:
        position += 1

    # Sätt in värdet på rätt position genom att använda set-metoden
    ulist.items.insert(position, value)
