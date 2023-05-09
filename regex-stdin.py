from https://wiki.python.org/moin/Powerful%20Python%20One-Liners

Apply regular expression to lines from stdin

[another command] | python -c "import sys,re;[sys.stdout.write(re.sub('PATTERN', 'SUBSTITUTION', line)) for line in sys.stdin]"
