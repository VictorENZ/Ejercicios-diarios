"""x = -657

#debtro del rango de 32bits "leetcode"
def reverseint(x):
 if x<=0:
   x =x*-1
   res= int(str(x)[::-1])*-1
 else:
   res= int(str(x)[::-1])
 return res if res< 2**31-1 and res> -2**31 else 0
   
print(reverseint(x))"""

