s = "abcdefgh"
t="abcdefghh"

def finddif(s,t):
  for i in t:
    if i not in s or t.count(i) > s.count(i):
      return i

print(finddif(s,t))