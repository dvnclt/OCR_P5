# Écrivez votre code ici !

def square(a):
    if isinstance(a, (int, float)):
        return a ** 2
    print("Le paramètre doit être un nombre !")
    return None


test1 = square(6)
print(test1)

test2 = 5
print(square(test2))

test3 = 2.2
print(square(test3))

test4 = square("test4")
print(test4)
