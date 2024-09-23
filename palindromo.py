palabra = input("ingresa una palabra o frase: ")
                
def palindromo(palabra):
  new = ""
  letras = "abcdefghijklmnopqrdtuvwxyz"
  for i in palabra.lower():
    if i in letras:
      new += i
  if new == new[::-1]:
     print(f"La frase: '{palabra}' es un palindromo")
  else:
     print(f"La frase: '{palabra}' no es un palindromo")

palindromo(palabra)