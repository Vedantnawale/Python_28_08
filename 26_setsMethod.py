s1 = {1,2,34,34,2,6}
s2 = {67,23,12,423,32,1}
# print(s1.union(s2))
# print(s1.intersection(s2))
# print(s1.symmetric_difference(s2))
print(s1.isdisjoint(s2))
s1.update(s2)
print(s1,s2)