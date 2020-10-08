def dupliques(li):
    res = ""
    for i in li:
        if li.count(i) != 1:
            res = True
            break
        else:
            res = False
    if li == "":
        res = False
    return res


print(dupliques(""))
