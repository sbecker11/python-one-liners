# from https://wiki.python.org/moin/Powerful%20Python%20One-Liners

fib = lambda n:reduce(lambda x,n:[x[1],x[0]+x[1]], range(n),[0,1])[0]

or

lambda x: x if x<=1 else fib(x-1) + fib(x-2)
