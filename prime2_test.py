from math import sqrt
for i in range(2,1000):
    flag=1
    k=int(sqrt(i))
    for j in range(2,k+1):
        if i%j==0:      
            flag=0
            break
    if(flag!=0):  
          print (i,)
    print('\n')


#continue 
suma=0
i=1
while i<=5:
  suma+=i
  i+=1
  if i==4:
       continue

print ('i=%d,sum=%d'%(i,suma))  

