# devolver la cantidad de elementos que no son iguales a n1
n1, nums = 3, [3,2,2,3]
def remove_element(n1,nums):
  n = 0
  for i in range(len(nums)):
    if nums[i] != n1:
      nums[n] = nums[i]
      n += 1
  return n

nq = remove_element(n1,nums)
print(nq)