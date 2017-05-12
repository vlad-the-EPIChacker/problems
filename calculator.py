def calc(e):
    a=0
    if e[0]=='-':
        c=-int(e[1])
        e=e[1:]
    elif e[0]=='+':
        c=int(e[1])
        e=e[1:]
    else:
        c=int(e[0])
    for i in range(1, len(e)):
        if e[i-1]=='*':
            c *= int(e[i])
        elif e[i-1]=='/':
            c /= int(e[i])
        elif e[i-1]=='+':
            a += c
            c=int(e[i])
        elif e[i-1]=='-':
            a+=c
            c=-int(e[i])
    a += c
    return a

e="-1*2+8/4"
print calc(e)