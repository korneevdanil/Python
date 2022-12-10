# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
for x in range(2):
        for y in range(2):
            for z in range(2):
                zn = not (x or y or z) == (not x and not y and not z)
                print("При x = " + str(x) + " y = " + str(y) + " z = " + str(z))
                print("Утверждение (¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z )" + str(zn))