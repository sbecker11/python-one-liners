from https://wiki.python.org/moin/Powerful%20Python%20One-Liners

Reverse lines in stdin

python -c "import sys; print '\n'.join(reversed(sys.stdin.read().split('\n')))"
