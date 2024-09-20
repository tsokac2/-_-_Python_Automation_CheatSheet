# List of Meta Characters

# .        Matches any single character
# \        Escapes one of the meta characters to treat it as a regular character
# [...]    Matches a single character or a range that is contained within brackets. Order does not matter but without brackets order does matter
# +        Matches the preeceding element one or more times
# ?        Matches the preeceding element zero or one time
# *        Matches the preeceding element zero or more times
# {m,n}    Matches the preeceding element at least m and not more than n times
# ^        Matches the beginning of a line or string
# $        Matches the end of a line or string
# [^...]   Matches a single character or a range that is not contained within the brackets
# ?:...|..."Or" operator
# ()       Matches an optional expression

import re

text = 
"""
Hi team. I am part of API integration Team tom@email=com, need a admin access to troubleshoot admin@airbnbcoworker.com partner cases and issues. Thank you.
"""
# pattern = re.compile("[a-z]+@[a-z]+.[a-z]+") # Email pattern

pattern = re.compile("[^ ]*@[^ ]+\.[a-z]+") 

matches = pattern.findall(text)
print(matches)
