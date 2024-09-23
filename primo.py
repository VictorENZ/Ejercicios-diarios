def primo():
  num = int(input("ingresa un numero: "))
  for i in range(2,num):
    if num % i == 0:
      return "no es primo"
  return "es primo"

es_primo=primo()
print(es_primo)