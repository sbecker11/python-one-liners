lst1 = [1, 2]
lst2 = ["x", "y"]
for x in lst1:
    for y in lst2:
        print(x, y)
#Output
# 1 x
# 1 y
# 2 x
# 2 y
#example Code of Single Line Loop
[print(x, y) for x in lst1 for y in lst2]
