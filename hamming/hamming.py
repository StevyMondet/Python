# distance de hamming entre deux mots

def distance_hamming(mots1, mots2):
    x = 0
    i = 0
    if len(mots1) == len(mots2):
        while i < len(mots1):
            if mots1[i] != mots2[i]:
                x = x + 1
            i = i + 1
        print("la distance de hamming entre {} et {} est de {}".format(mots1, mots2, x))
    else:
        print("les mots n'ont pas la même longueur, impossible de calculer la distance de hamming")


mot1 = input("entrez le premier mot\n")
mot2 = input("entrez le deuxieme mot\n")

distance_hamming(mot1, mot2)