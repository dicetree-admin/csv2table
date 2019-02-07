total = []
a = [['aa','b',4], ['c','d',1]]
b = [['bb','b',2], ['c','d',5]]
c = [['cc','f',3], ['g','h',13]]
d = [['dd','g',1], ['a','b',11]]
total_base = total


# print(a+b)
# print(totalL )


def listMaxExchange(listA, listB, target_col=4):
    # 0컬럼 반영
    target_col = target_col - 1

    for row in listA:
        print(row)

    for i in range(len(listA)):
        print(listA[i][target_col])
        print(listB[i][target_col])

        if listA[i][target_col] < listB[i][target_col]:
            listA[i] = listB[i]
    return listA


listA = listMaxExchange(total_base, a, 3)
print(listA)
listA = listMaxExchange(a, b, 3)
print(listA)
listA = listMaxExchange(listA, c, 3)
print(listA)
listA = listMaxExchange(listA, d, 3)
print(listA)