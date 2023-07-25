# somemodule.py

def spam():
    pass

def grok():
    pass

blah = 42

# Only export 'spam' and 'grok'
# 限制导出的范围
__all__ = ['spam', 'grok']