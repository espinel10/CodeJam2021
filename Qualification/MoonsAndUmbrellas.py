def cost(arr,X,Y):
    acum=0
    for i in range(0,len(arr)-1):
        if arr[i]+arr[i+1]=='CJ':
            acum=acum+X
        elif arr[i]+arr[i+1]=='JC':
            acum=acum+Y
    return acum

def opcion(a,b,X,Y):
  selC=0
  selJ=0
  if a!=None and b!=None:
    if a==b:
        return a
  if a!=None:
    if a+'C'=='JC':
      selC=selC+Y
  if b!=None:
    if 'C'+b=='CJ':
      selC=selC+X
  if a!=None:
    if a+'J'=='CJ':
      selJ=selJ+X
  if b!=None:
    if 'J'+b=='JC':
      selJ=selJ+Y
  
  if selC>selJ:
    return 'J'
  else:
    return 'C'

def solve(X,Y,S):
    indices=[]
    ent=list(S)
    income=0
    indi=[]
    for i in range(len(ent)):
        #print("#############")
        #print(ent[i])
        #print(indi)
        if ent[i]=='?':
            indi.append(i)
        else:
          if len(indi)>0:
              indices.append(indi[:])
              indi.clear()
    if len(indi)>0:
      indices.append(indi[:])

    for i in indices:
      a,b=None,None
      if i[0]-1>-1:
        a=ent[i[0]-1]
      if i[-1]+1<len(ent):
        b=ent[i[-1]+1]
      desc=opcion(a,b,X,Y)
      for kk in i:
        ent[kk]=desc

    #print(indices)
    #print(ent)
    return cost(ent,X,Y)

T=int(input().strip())
for i in range(1, T+1):
    input1=list(input().split(" "))
    X=int(input1[0])
    Y=int(input1[1])
    S=list(input1[2])
    #print(input1)
    print("Case #"+str(i)+": "+str(solve(X,Y,S)))