def intersection(v, w):
    """renvoie l'intersection entre deux mots"""

    # initialise un mot_max
    mot_max = ''

    # chaque combinaison de syllabe va être vérifié
    for i in range(len(v)):
        for j in range(len(v) + 1):
            # si la syllabe est dans w et plus grande que mot_max, il le remplace
            if (v[i:j] in w) and len(v[i:j]) > len(mot_max):
                mot_max = v[i:j]

    return mot_max


print(intersection("programme", "grammaire"))
