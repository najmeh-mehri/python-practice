#Check Password
p = input()
a=0
flag = 0
if p =='':
    print('required errors')
else:
    if len(p)<8 or len(p)> 64:
        print('invalid length')
        flag = 1
    for i in p:
        if  48<=ord(i)<=57:
            a += 1
    if a == 0 :
        flag = 1
        print('password must contain digit')
    a = 0
    for i in p :
        if  65<=ord(i)<=90 or 97<=ord(i)<=122:
            a += 1
    if a == 0:
        flag = 1
        print('password must contain alphabet')
    if flag == 0 :
        print('valid password')