n1,n2=[1,3,4],[2]

def addtwosum(n1,n2):   
   n4 =n3 = ""
   n5,i = [],0
   n1,n2 = n1[::-1],n2[::-1]
   
   if len(n1) > len(n2):
       max = len(n1)
   else: 
       max = len(n2)

   while i < max:
      if i < len(n1):
         n3 += str(n1[i])
      if i < len(n2):
         n4 += str(n2[i])
      i +=1
   res = int(n3) + int(n4)
   
   for c in str(res):
      n5.append(c)
   
   return n5[::-1]
   
print(addtwosum(n1,n2))
