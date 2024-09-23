def fibonacci():
  x = input("¿Cuanto numeros quieres visualizar?: ")
  a,b=0,1
  i= 0
  while i < int(x):
    print(a)
    a,b = b, a+b
    i += 1

fibonacci()