import gzip
with gzip.open('somefile.gz', 'rt') as f:
    text = f.read()


import bz2
with bz2.open('somefile.bz2', 'rt') as f:
    text = f.read()

import gzip
with gzip.open('somefile.gz', 'wt') as f:
    f.write(text)

import bz2
with bz2.open('somefile.bz2', 'wt') as f:
    f.write(text)