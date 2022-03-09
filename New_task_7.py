# Проверить истинность утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат
X = [False, True]
Y = [False, True]
Z = [False, True]
print('X\t\tY\t\tZ\t\tResult')
for i in X:
    for j in Y:
        for k in Z:
            if (not(X or Y or Z)) == (not X and not Y and not Z):
                print(f'{i}\t{j}\t{k}\tTrue')
            else:
                print(f'{i}\t{j}\t{k}\tFalse')
