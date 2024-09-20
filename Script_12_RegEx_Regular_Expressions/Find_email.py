# Write a regular expression that returns all the list items that contain Delhi and an email address.

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
# Your solution should output the following:

# ['mrs Anna Cloudy, Delhi, 2dogs 1fish bathlover@example.com']

import re
 
pattern = re.compile(".*Delhi.*[^ ]+@[^ ]+\.[a-z]+", re.IGNORECASE)
matches = [match for match in data if pattern.findall(match)]
print(matches)

# Explanation:

# .*Delhi.* searches for Delhi anywhere in the line.

# [^ ]+ searches for one or more characters other than white space.

# @[^ ]+ searches for an @ symbol followed by any number of characters other than space.

# \.[a-z]+ searches for a dot followed by any number of letters.