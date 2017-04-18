def noHex(h):
    h=h.lstrip('0x').upper()
    h=list(h)
    f=0
    for i in range(0, len(h)):
        if h[i].isdigit():
            ih = ord(h[i])-ord('0')
        elif ord(h[i])<=ord('F') and ord(h[i])>=ord('A'):
            ih = ord(h[i])-ord('A')+10
        else:
            raise ValueError('invalid')
        h[i]=ih
    f=h[0]
    for i in range(1, len(h)):
        f=f*16
        f=f+h[i]
    return f


if noHex('0xF')!=15:
    print 'hex 0xF failed'
else:
    print 'hex 0xF sucess'
if noHex('0x1F')!=31:
    print 'hex 0xF failed'
else:
    print 'hex 0xF sucess'
try:
    noHex('0xl')
    print 'failed'
except:
    print 'sucess'
if noHex('0x1f')!=31:
    print 'hex 0xF failed'
else:
    print 'hex 0xF sucess'