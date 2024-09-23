num, nums = 8, [2, 6, 7, 4]

def sum(num, nums):
  dic={}
  for i,n in enumerate(nums):
    a = num - n
    if a in dic:
      return[dic[a], i]
    dic[n]=i
  
n3 = sum(num, nums)
print(n3)
