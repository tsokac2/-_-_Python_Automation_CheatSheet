# Write a regular expression that returns all the list items that contain the word Delhi. The list is stored in the data variable:

data=[
    "mr Jim Cloudy, Texas, 01091231, 1 dog 1 cat, jim.cloudy@example.com", 
    "mrs Anna Cloudy, Delhi, 2dogs 1fish bathlover@example.com",
    "Mrs. Sarah Prost, Baghdad, +4327629101, 1 hamster, 2 crocodiles",
    "Ms Beta Palm Ontario 08234211 12 cats, beta@example.com",
    "mr. Dog Bells texas 09234211 3 honey badgers alta_bells.example.com",
    "ms. Claudia More, Gujarat, 012311, 3 dogs",
    "mrs Alma Stills Delhi 01231981 1 dog",
    "mr Sen Kumar Delhi 3456 ants"
]
# Your code solution output the following:

['mrs Anna Cloudy, Delhi, 2dogs 1fish bathlover@example.com',
 'mrs Alma Stills Delhi 01231981 1 dog',
 'mr Sen Kumar Delhi 3456 ants']

import re
 
pattern = re.compile(".*Delhi.*", re.IGNORECASE)
matches = [match for match in data if pattern.findall(match)]
print(matches)


# .*Delhi.* instructs the program that Delhi could be found between any number of characters. 
# The part .* means there could be any number of characters before or after Delhi. 
# The expression .*Delhi.* could also be replaced with just Delhi and still produce the same result, but 
# .*Delhi.* is more explicit and more logical.