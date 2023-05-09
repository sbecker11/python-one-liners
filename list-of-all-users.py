# from https://wiki.python.org/moin/Powerful%20Python%20One-LinersA

print '\n'.join(line.split(":",1)[0] for line in open("/etc/passwd"))
