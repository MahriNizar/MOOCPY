import random

# def pierre_Feuille_ciseaux(x,t,):
#     sco = 0
#     li = [j1,j2,j3,j4,j5]
#     play = li[i]
#     if play == 0 and x==2:
#         sco += 1
#         res = "Pierre bat Ciseaux : {score += sco}".format(sco) 
#     elif play == 1 and x==0:
#         sco += 1
#         res = "Feuille bat Pierre : {score += sco}".format(sco)
#     elif play == 2 and x ==1:
#         sco += 1
#         res = "Ciseaux bat Feuille : {score += sco}".format(sco)
#     elif play == 0 and x ==1:
#         sco -= 1
#         res = "Pierre est battu par Feuille : {score += sco}".format(sco)
#     elif play == 1 and x==2:
#         sco -= 1
#         res = "Feuille est battu par Ciseaux : {score += sco}".format(sco)
#     elif play == 2 and x ==0:
#         sco -= 1
#         res = "Ciseaux est battu par Pierre : {score += sco}".format(sco)
#     elif play==0 and x ==0:
#         sco += 0
#         res = "Pierre annule Pierre : {score += sco}".format(sco)
#     elif play==1 and x==1:
#         sco += 0
#         res = "Feuille annule Feuille : {score += sco}".format(sco)
#     elif play ==2 and x==2:
#         sco+=0
#         res = "Ciseaux annule Ciseaux : {score += sco}".format(sco)
    # return res
score = 0
s= int(input())
random.seed(s)
j1= int(input())
j2= int(input())
j3= int(input())
j4= int(input())
j5= int(input())
for i in range(5):
    x = random.randint(0,2)
    sco = 0
    li = [j1,j2,j3,j4,j5]
    play = li[i]
    if play == 2 and x==0:
        sco -= 1
        score+=sco
        print(f"Pierre bat Ciseaux : {score}")
    elif play == 0 and x==1:
        sco -= 1
        score+=sco
        print(f"Feuille bat Pierre : {score}")
    elif play == 1 and x ==2:
        sco -= 1
        score+=sco
        print(f"Ciseaux bat Feuille : {score}")
    elif play == 1 and x ==0:
        sco += 1
        score+=sco
        print(f"Pierre est battu par Feuille : {score}")
    elif play == 2 and x==1:
        sco += 1
        score+=sco
        print(f"Feuille est battu par Ciseaux : {score}")
    elif play == 0 and x ==2:
        sco += 1
        score+=sco
        print(f"Ciseaux est battu par Pierre : {score}")
    elif play==0 and x ==0:
        
        score += 0
        print(f"Pierre annule Pierre : {score}")
    elif play==1 and x==1:
        
        score += 0
        print(f"Feuille annule Feuille : {score}")
    elif play ==2 and x==2:
        
        score -=0 
        print(f"Ciseaux annule Ciseaux : {score}")
    
    
if score  >0:
    print("Gagné")
elif score ==0:
    print("Nul")
else:
    print("Perdu")