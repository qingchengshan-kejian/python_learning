s = "Look into my eyes, look into my eyes, the eyes, the eyes, \
the eyes, not around the eyes, don't look around the eyes, \
look into my eyes, you're under."

import textwrap
print(textwrap.fill(s, 70))
print(textwrap.fill(s, 40))
# 首行缩进
print(textwrap.fill(s, 40, initial_indent='    '))

# 除首行外缩进
print(textwrap.fill(s, 40, subsequent_indent='    '))