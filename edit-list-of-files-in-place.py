# from https://wiki.python.org/moin/Powerful%20Python%20One-Liners

Editing a list of files in place
I came up with this one-liner in response to an article that said it couldn't be done as a one-liner in Python.

What this does is replace the substring "at" by "op" on all lines of all files (in place) under the path specified (here, the current path).

Caution: Don't run this on your home directory or you're going to get all your text files edited.


import sys,os,re,fileinput;a=[i[2] for i in os.walk('.') if i[2]] [0];[sys.stdout.write(re.sub('at','op',j)) for j in fileinput.input(a,inplace=1)]
Clearer is: import os.path; a=[f for f in os.listdir('.') if not os.path.isdir(f)]

