tmp = [1,2,3,4,5,6,7]

fromidx = 6
toidx = 1
tmpval = tmp[fromidx]

# del tmp[fromidx]
# tmp.insert(toidx, tmpval)
#
# print tmp

newlst = []

for idx, val in enumerate(tmp):
    if idx == fromidx:
        continue
    if idx == toidx:
        newlst.append(tmpval)
    newlst.append(val)

print newlst