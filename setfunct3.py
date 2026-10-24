set1={1, 2, 3, 4, 5}
set2={3, 4, 5, 6, 7}
set3={4, 5, 8, 9}
common=set1&set2&set3
print("Common elements:",common)
only_one=(set1-set2-set3)|(set2-set1-set3)|(set3-set1-set2)
print("Elements present in only one set:", only_one)




if set1&set2&set3==set():
    print("The sets are disjoint")
else:
    print("The sets are not disjoint")

symetricdiff=(set1-set2)|(set2-set1)
print("Symmetric difference:",symetricdiff )

