# from https://wiki.python.org/moin/Powerful%20Python%20One-Liners

Find All Indices of an Element in a List
Say, you want to do the same as the list.index(element) method but return all indices of the element in the list rather than only a single one.

In this one-liner, you’re looking for element 'Alice' in the list lst = [1, 2, 3, 'Alice', 'Alice'] so it even works if the element is not in the list (unlike the list.index() method).


Toggle line numbers
   1 # List
   2 lst = [1, 2, 3, 'Alice', 'Alice']
   3 
   4 # One-Liner
   5 indices = [i for i in range(len(lst)) if lst[i]=='Alice']
   6 
   7 # Result
   8 print(indices)
   9 # [3, 4]
