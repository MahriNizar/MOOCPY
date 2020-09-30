def rendre_monnaie(prix,x20,x10,x5,x2,x1):
    a,b,c,d,e = x20*20,x10*10,x5*5,x2*2,x1
    somme_argent = a+b+c+d+e 
    if somme_argent < prix:
        return (None,None,None,None,None)
    else:
        somme_argent -= prix
        b20 = (somme_argent -(somme_argent % 20))/20
        b10 = int(10-((somme_argent%20) %10))
        b5 = int((somme_argent%20)/5)
        b2 = int((somme_argent%20)/2)
        b1 = ((((somme_argent%20) %10)%5)%2)
        return (b20,b10,b5,b2,b1)
print(rendre_monnaie(100,0,14,5,5,1))
"3.1.1.0.1"