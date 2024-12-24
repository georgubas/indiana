par = []
print('Введите число:')
n = int(input())
for j in range(1,n):
    for c in range(j+1,n):
        if n % (j + c) == 0:
         b = str(j)+str(c)
         par.append(b)
print('Если в столбце цифра',n,'то пароль: ',*par)