# Write a regular expression that returns all the list items that contain Delhi, and have either a phone number or an email address.

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
# ['mrs Anna Cloudy, Delhi, 2dogs 1fish bathlover@example.com',
#  'mrs Alma Stills Delhi 01231981 1 dog']

import re
 
pattern = re.compile(".*Delhi.*([0|+][0-9]{4,50}|[^ ]+@[^ ]+.[a-z]+)", re.IGNORECASE)
matches = [match for match in data if pattern.findall(match)]
print(matches)

# Explanation:
# .*Delhi.* searches for Delhi anywhere in the line.
# [0|+][0-9]{4,50} searches for a 0 or a + followed a number of 4 to 50 digits.
# | makes the preceding and proceeding patterns optional.
# [^ ]+@[^ ]+.[a-z]+ searches for email addresses.
# ( ) are part of the ( | ) "OR" syntax.