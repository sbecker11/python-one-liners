 # from https://wiki.python.org/moin/Powerful%20Python%20One-Liners

 # Quicksort Python One-liner
  lambda L: [] if L==[] else qsort([x for x in L[1:] if x< L[0]]) + L[0:1] + qsort([x for x in L[1:] if x>=L[0]])
