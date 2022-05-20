st = input()
u=l=a=d=0
for i in range(len(st)):
    if(st[i].isupper()):
        u=u+1
    if(st[i].islower()):
        l=l+1
    if(st[i].isalpha()):
        a=a+1
    if(st[i].isdigit()):
        d=d+1
print('Number of uppercase letters',u)
print('Number of lowercase letters',l)
print('Number of alphabets letters',a)
print('Number of digits letters',d)