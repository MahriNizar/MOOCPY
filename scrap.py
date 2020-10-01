def bat(j1,j2):

    if (j1 ==0 and j2==2) or (j1==1 and j2==0) or (j1==2 and j2==1):
        res = True
    else:
        res=False
    return res

print(bat(2,1))