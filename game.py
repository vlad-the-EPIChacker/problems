f=open('gamereviews.dat')
file=f.readlines()
nfile=int(file[0])
games={}
names=[]

for i in range(1, nfile+1):
    line=file[i].strip()
    line=line.split(', ')
    line=line[1:]
    name=line[0]
    score=int(line[1])
    if not name in games.keys():
        games[name]=[0, 0]
        names.append(name)
    games[name][0]+=score
    games[name][1]+=1

names=sorted(names)

for i in names:
    ave=float(games[i][0])/games[i][1]
    ave=round(ave, 1)
    print i, ave