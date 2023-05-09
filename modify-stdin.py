from https://wiki.python.org/moin/Powerful%20Python%20One-Liners

Modify lines from stdin using map

python -c "import sys; tmp = lambda x: sys.stdout.write(x.split()[0]+'\t'+str(int(x.split()[1])+1)+'\n'); map(tmp, sys.stdin);"
