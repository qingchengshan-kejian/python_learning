# mypackage/
#   __init__.py
#   A/
#      __init__.py
#      spam.py
#      grok.py
#   B/
#      __init_.py
#      bar.py

# mypackage/A/spam.py
from . import grok

# mypackage/A/spam.py
from ..B import bar

