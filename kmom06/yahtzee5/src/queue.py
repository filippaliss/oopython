"""
Lägg till stöd för flera spelare med hjälp av en kö för att hålla koll på vilken spelares tur det är. Ni gör det genom att använda dequeue/peek för att få ut nuvarande spelare och enqueue för att lägga till spelare sist igen.

Om ni gjorde extrakravet i kmom05 och implementerade en egen Queue klass, kopiera in den filen i src och använd den. Annars, kopiera koden från Datastrukturer#Queue och lägg i src/queue.py.

Jag rekommenderar att skapa en to_list() metod i Queue klassen så ni enkelt kan få ut datan för att spara i session.
Och en metod så ni kan återskapa Queue klassen från session datan.
Ni får inte ändra mer i Queue klassen. Den ska uppfylla metoderna för en abstrak Queue klass. Den ska inte implementeras för att specifik hålla två spelare.
"""