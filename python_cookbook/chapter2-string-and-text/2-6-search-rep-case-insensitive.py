import re

text = 'UPPER PYTHON, lower python, Mixed Python'
find1 = re.findall('python', text, flags=re.IGNORECASE)
print(find1)
sub1 = re.sub('python', 'snake', text, flags=re.IGNORECASE)
print(sub1)

def matchcase(word):
    def replace(m):
        text = m.group()
        if text.isupper():
            return word.upper()
        elif text.islower():
            return word.lower()
        elif text[0].isupper():
            return word.capitalize()
        else:
            return word
    return replace
# 返回函数的函数

print(re.sub('python', matchcase('snake'), text, flags=re.IGNORECASE))


