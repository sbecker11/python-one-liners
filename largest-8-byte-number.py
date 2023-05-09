# from https://wiki.python.org/moin/Powerful%20Python%20One-Liners

Largest 8-Bytes Number
And what's the largest number that can be represented by 8 Bytes?


print '\n'.join("%i Byte = %i Bit = largest number: %i" % (j, j*8, 256**j-1) for j in (1 << i for i in range(8)))
