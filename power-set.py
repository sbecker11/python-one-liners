# from https://wiki.python.org/moin/Powerful%20Python%20One-Liners

# Power set Python One-Liner
lambda l: reduce(lambda z, x: z + [y + [x] for y in z], l, [[]])
