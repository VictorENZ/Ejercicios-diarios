a= input("ingresa una palabra: ")
b= input("ingresa otra palabra: ")

def anagrama(a, b):
  a= "".join(sorted(a.lower()))
  b= "".join(sorted(b.lower()))
  if a == b:
    return "Es anagrama"
  return "No es anagrama"

print(anagrama(a, b))