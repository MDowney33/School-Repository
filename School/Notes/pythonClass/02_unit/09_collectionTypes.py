# str, list, tuple, set, dictionary
#tuple is not mutable (,) useful for immutable single peace of data ex(x,y)
#types of elements: Hashable (must be immutable), not ordered, distinct (no duplicates) {,}
#dictionary, hashable,  not really ordered {:}
from time import perf_counter
users=1000
usersList=set([x for x in range(users)])
t1=perf_counter()
print(users in usersList)
t2=perf_counter()
print((t2-t1) *1000)
