# from https://wiki.python.org/moin/Powerful%20Python%20One-Liners

python -c 'import re,sys;print re.sub("\s*([{};,:])\s*", "\\1", re.sub("/\*.*?\*/", "", re.sub("\s+", " ", sys.stdin.read())))'

