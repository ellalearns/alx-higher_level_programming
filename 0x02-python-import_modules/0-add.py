
alist = ['r', 'c', 'a', 'b', "C", "a", 'c']
while "c" in alist:
    del alist[alist.index('c')]

while "C" in alist:
    del alist[alist.index('C')]

print(alist)
