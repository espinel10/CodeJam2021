def reverse(ent,i,j):
  sal=ent[:]
  vals=ent[i:j]
  vals.reverse()
  sal[i:j]=vals
 
  return sal[:]


def solve(arr):
  acum=0
  for i in range(0,len(arr)-1):
    j=arr.index(min(arr[i:]))
    arr=reverse(arr,i,j+1)

    acum=acum+((j+1)-(i+1)+1)
  return acum

T=int(input().strip())

for i in range(1, T+1):
    N=int(input().strip())
    input1=list(map(int,input().split(" ")))
    resp=solve(input1)
    print("Case #"+str(i)+": "+str(resp))

        