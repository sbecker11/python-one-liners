# from https://wiki.python.org/moin/Powerful%20Python%20One-Liners

Retrieve content text from HTTP data

python -c "import sys; print sys.stdin.read().replace('\r','').split('\n\n',2)[1]";
