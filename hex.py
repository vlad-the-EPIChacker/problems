def hexa(n):
    final=''
    letters=['A', 'B', 'C', 'D','E', 'F']
    if n>9:
        final=str(letters[n-10])
    else:
        final=str(n)
    return final

def hex1(n):
    oxn=''
    neg=False
    if n==0:
        return '0x0'
    if n<0:
        neg=True
        n=-n
    while n>0:
        d=hexa(n%16)
        oxn=d+oxn
        n=n/16
    oxn='0x'+oxn if not neg else '-0x'+oxn
    return oxn


if hex1(15)!='0xF':
    print 'hex 15 failed'
else:
    print 'hex 15 sucess'
if hex1(4095)!='0xFFF':
    print 'hex 4095 failed'
else:
    print 'hex 4095 sucess'
if hex1(-15)!='-0xF':
    print 'hex -15 failed'
else:
    print 'hex -15 sucess'
if hex1(0)!='0x0':
    print 'hex 0 failed'
else:
    print 'hex 0 sucess'
if hex1(1234567)!='0x12D687':
    print 'hex 1234567 failed'
else:
    print 'hex 1234567 sucess'


