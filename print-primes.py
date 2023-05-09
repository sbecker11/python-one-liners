# https://medium.com/@chenyumei8866/20-extremely-useful-single-line-python-codes-bc553ea4832a
# Find primes between 2 and 19 in a single line of code
print(list(filter(lambda a: all(a % b != 0 for b in range(2, a)), range(2,20))))  
# print
# [2, 3, 5, 7, 11, 13, 17, 19]
