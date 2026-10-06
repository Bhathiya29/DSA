# Hashset

s = set()
print(s)


# Adding items to the set
s.add(1)
s.add(2)
s.add(3)


# Lookup if item in set 
if 1 not in s:
    print(True)

string = 'aaaaaaaaaaabbbbbbbbbbbbbbcccccccccccccceeeeeeeeeeeeee'

sett = set(string)

sett

# Hashmaps - Dictionaries

d ={'a':1, 'b':2, 'c':3}

# Adding key value pairs
d['e'] = 4

print(d)

print(d['a'])

# Loop over the key val pairs of the dictionary
for key, value in d.items():
    print(f"key{key} value{value}")


# Default Dict

from collections import defaultdict

default_dict = defaultdict(list)

# counter dict
from collections import Counter
counter = (Counter(string))

counter
