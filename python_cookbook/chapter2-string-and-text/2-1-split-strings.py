line = 'asdf fjdk; afed, fjek,asdf,    foo'
import re
line_r = re.split(r'[;,\s]\s*', line)
print(line_r)