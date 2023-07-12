# def avg(first, *rest):
#     return(first + sum(rest)) / (1 + len(rest))
#
# print(avg(1, 2))
# print(avg(1, 2, 3, 4, 5))


import html

def make_element(name, value, **attrs):
    keyvals = [' %s=%s ' % item for item in attrs.items()]
    attr_str = ''.join(keyvals)
    element = '<{name}{attrs}>{value}</{name}>'.format(
        name=name,
        attrs=attr_str,
        value=html.escape(value)
    )
    return element

# demo
s = make_element('item', 'Albatross', size='large', quantity=6)
print(s)

def anyarg(*args, **kwargs):
    print(args) // tuple
    print(kwargs) // dict