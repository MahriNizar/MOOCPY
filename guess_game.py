import random
random.seed(1)
to_guess = random.randint(0,100)
essaie = 6
print(to_guess)
guess = int(input())
compt = 1
if guess == to_guess:
    print(f"Gagné en 1 essais !")
elif guess != to_guess:
    for i in range(5):
        compt = compt + 1
        if guess < to_guess:
            print("Trop petit")
            guess = int(input())
        else:
            print("Trop grand")
            guess = int(input())
        if guess == to_guess:
            print(f"Gagné en {compt} essais !")
if guess != to_guess:
    print(f"Perdu ! Le secret était {to_guess}")
