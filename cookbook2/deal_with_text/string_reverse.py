#!/usr/bin/python

astring = 'helllo world'

# reverse by char
revchars = astring[::-1]
print(revchars)

# reverse by word
revwords = astring.split( )
revwords.reverse()
revwords = ' '.join(revwords)
print(revwords)

# reverse by word 2
revwords = ' '.join(astring.split( )[::-1])
print(revwords)

# reverse by word 3
import re
revwords = re.split(r'(\s+)', astring)
revwords.reverse()
revwords = ''.join(revwords)
print(revwords)
