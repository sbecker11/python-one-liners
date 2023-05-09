# from https://wiki.python.org/moin/Powerful%20Python%20One-Liners

python -c "print ''.join(chr(int(''.join(i), 16)) for i in zip(*[iter('474e552773204e6f7420556e6978')]*2))"

