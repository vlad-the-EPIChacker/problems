def comma(flt):
    flt=str(flt)
    if len(flt)>4:
        return flt
    if len(flt)>3:
        flt=list(flt)
        flt1=flt[:3]
        ','.append(flt1)
        flt2=flt[3:]
        flt=''.join(flt1)+''.join(flt2)
    if len(flt)>6:
        flt = list(flt)
        flt1 = flt[:6]
        ','.append(flt1)
        flt2 = flt[6:]
        flt = ''.join(flt1) + ''.join(flt2)
    return flt


f=open("accounting.dat")
file=f.readlines()
balance=0

print '****.'*8
print ' '*7, 'Transaction : Balance'

for i in range(0, len(file)):

    file[i]=file[i].lstrip('$')
    file[i]=file[i].replace(',', '')

    if file[i][0]=='(':
        file[i]=list(file[i])
        file[i][0]=''
        file[i][len(file[i])-2]=''
        file[i]=''.join(file[i])
        file[i]=float(file[i])*-1
    else:

        file[i]=float(file[i])
    transaction=str(file[i])
    balance=balance+float(transaction)
    if transaction[0]=='-':
        transaction=transaction.replace('-', '(')
        transaction=transaction+')'

    x=18-len(transaction)
    balance=str(balance)
    if balance[0]=='-':
        balance=balance.replace('-', '(')
        balance=balance+')'
    transaction1=comma(transaction)
    balance1=comma(balance)
    final=''
    final=x*' '+'$'+transaction1+' : '+balance1
    balance = list(balance)
    balance[0] = ''
    balance[len(balance)-1] = ''
    balance = ''.join(balance)
    balance = float(balance) * -1
    print final

print '****.'*8