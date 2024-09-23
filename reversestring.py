x = "amo la paloma"

k, text = 2,"abcdefg"
if k > 0:
  a=text[:k]
  a=a[::-1]
  text=text.replace("ab",a)
  print(text)
else:
  print(text[::-1])

def reversestring(x):
   return True if x == x[::-1] else False

reversestring(x)