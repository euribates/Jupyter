## Diccionarios (Hashmaps)

La última estructura de datos de tipo colección que veremos es el
**diccionario**. The previous collections we looked at have all been sequence
collections, because the values are in a sequence from first to last and you
access them by their position within the list. Dictionaries are mapping
collections because they map one piece of information to another. We could use
a dictionary to store the prices of our shopping list by mapping the name of
the food item to its price.  Let’s say that fugu costs $100 and ramen costs $5;
we can create a dictionary that holds this information as follows:

    >>> my_dictionary={'ramen': 5.0, 'fugu': 100.0}

The curly braces create a dictionary. Inside the braces we have the string
'ramen' followed by a colon, then the number 5.0 (price in dollars). This tells
Python that the string maps to the number; in other words, we can look up the
price if we have the name of the food item. Multi- ple items in a dictionary
are separated with a comma; in this example we have a second item that maps
'fugu' to the value $100.0$.

To retrieve that information, we use the square brackets ([]) operator again,
passing in the key we want to search for (in this case the key is either fugu
or ramen). The dictionary returns the value associated with the key—the price
of the item. Let’s look up our two keys:

    >>> my_dictionary['fugu']
    100.0
    >>> my_dictionary['ramen']
    5.0

You can also add new items to the dictionary by assigning new values to it:

    >>> my_dictionary['chopsticks']=7.50
    >>> my_dictionary['sake']=19.95
    >>> my_dictionary
    {'sake': 19.0, 'ramen': 5.0, 'chopsticks': 7.5, 'fugu': 100.0}

Here we have added two new items to the dictionary. You may have noticed that
when Python displays the list for us, the items are in a different order than
the way we originally created it. This is because dictionaries don’t have any
notion of order for keys in a dictionary.

