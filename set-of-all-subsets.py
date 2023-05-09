# from https://wiki.python.org/moin/Powerful%20Python%20One-Liners

Set of all subsets
Function that returns the set of all subsets of its argument

f = lambda x: [[y for j, y in enumerate(set(x)) if (i >> j) & 1] for i in range(2**len(set(x)))]

>>>f([10,9,1,10,9,1,1,1,10,9,7])
[[], [9], [10], [9, 10], [7], [9, 7], [10, 7], [9, 10, 7], [1], [9, 1], [10, 1], [9, 10, 1], [7, 1], [9, 7, 1], [10, 7, 1], [9, 10, 7, 1]]


f = lambda l: reduce(lambda z, x: z + [y + [x] for y in z], l, [[]])
