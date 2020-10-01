import math
def rac_eq_2nd_deg(a,b,c):
    if b**2-(4*a*c)>0:
        racines = math.sqrt(b**2-(4*a*c))
        rac1 = (-b+racines)/(2*a)
        rac2 = (-b-racines)/(2*a)
        return min(rac1,rac2),max(rac1,rac2)
    elif b**2-(4*a*c)==0:
        return (-b/(2*a),)
    else:
        return ()

print(rac_eq_2nd_deg(5,-3,-1.5))