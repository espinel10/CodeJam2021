def reverse(ent,i,j):
  sal=ent[:]
  vals=ent[i:j]
  vals.reverse()
  sal[i:j]=vals
  return sal[:]

class Revert:
  def __init__(self,N,C):
    self.C=C
    self.N=N
    self.respuesta=None
    self.recursion(0,0,[])
    


  def get_sol(self):
    if self.respuesta==None:
      return "IMPOSSIBLE"
    sol=[i+1 for i in range(self.N)]
    self.respuesta.reverse()
    for step in self.respuesta:
      j=step[1]-1
      i=step[0]-1
      sol=reverse(sol,i,j+1)
    return " ".join(list(map(str,sol)))

  def recursion(self,costo,i,memo):
    if costo>self.C:
      
      return
    if i==self.N-1:
      if costo==self.C:
        self.respuesta=memo[:]
      return
    for j in range(i,self.N):    
      income=(j+1)-(i+1)+1
      mem=memo[:]
      mem.append((i+1,j+1))
      self.recursion(ct+income,i+1,mem)




      

T=int(input().strip())
for i in range(1, T+1):
    N,C=input().split(" ")
    N=int(N)
    C=int(C)
    obj=Revert(N, C)
    print("Case #"+str(i)+": "+obj.get_sol())

        