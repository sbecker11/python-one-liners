# from https://wiki.python.org/moin/Powerful%20Python%20One-Liners

Reimplementing cut
Print every line from an input file but remove the first two fields.

python -c "import sys;[sys.stdout.write(' '.join(line.split(' ')[2:])) for line in sys.stdin]" < input.txt
