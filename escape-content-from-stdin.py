from https://wiki.python.org/moin/Powerful%20Python%20One-Liners

Escapes content from stdin
This can be used to convert a string into a "url safe" string

python -c "import urllib, sys ; print urllib.quote_plus(sys.stdin.read())";
