def palindrome(mot):
    i = 0
    test = 1
    long = len(mot)

    while i < long:
        if (mot[i] != mot[-i -1]):
            test = 0
        i = i + 1

    if (test == 1):
        print("palindrome")
    else:
        print("pas palindrome")

palindrome(input("entrez un mot :"))