list =[1,1,2,3,4,2,0,8,7,8]
list1 = []
list3 = [1,1,2,3,6,4,0,0,6,9,3,7]
print(list3)
print(list)

for i in list:
  if i not in list1:
    list1.append(i)
list3= list1
print(list3)

#elimina duplicados y ordena en Creciente pero no debuelve una lista
list2=set(list)
print(list2)

#elimina duplicados PERO desordena el orden original
for i in list:
  while list.count(i) > 1: #"Mientras en la lista el valor (i) se repita mas de "1" veces;No pares "
    list.remove(i) #elimina valor"i"
print(list)

