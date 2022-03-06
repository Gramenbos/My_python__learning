# Проверить истинность утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат
X = [False, True]
Y = [False, True]
Z = [False, True]
for i in X:
    for j in Y:
        for k in Z:
            if (not(X or Y or Z)) == (not X and not Y and not Z):
                print(True)
            else:
                print(False)
