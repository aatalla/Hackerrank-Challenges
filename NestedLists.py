Name=""
j=0
lstAll=[]
lstNames=[]
lstScores=[]
lstAlphabetical=[]
n=int(raw_input())
for i in range(n):
    name = raw_input()
    score = float(raw_input())
    lstAll.append(name)
    lstAll.append(score)
for e in range(0,2*n,2):
    lstNames.append(lstAll[e])
    lstScores.append(lstAll[e+1])
for a in range(n):
    for b in range(n):
        if lstScores[b]>lstScores[a]:
            j=lstScores[a]
            lstScores[a]=lstScores[b]
            lstScores[b]=j
            Name=lstNames[a]
            lstNames[a]=lstNames[b]
            lstNames[b]=Name
for u in range(0,n-1):
    if lstScores[u+1]==lstScores[u]:
        lstAlphabetical.append(lstNames[u])
    if lstScores[u]<lstScores[u+1] and u>=1:
        lstAlphabetical.append(lstNames[u])
        break
lstAlphabetical.sort()
for y in range(len(lstAlphabetical)):
    print lstAlphabetical[y]
