n = 56789 # 67895, 68957, 68579, 68597

def rotate_max(n):
   n = [i for i in str(n)]
   c ,i= [],0
   while i < len(n)-1:
       b = "".join(n)
       c.append(b)
       n.append(n[i])
       n.remove(n[i])
       i += 1
   return int(max(c))

d = rotate_max(n)
print(type(d))