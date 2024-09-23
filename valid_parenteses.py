parentesis= "(){[]}()]"

def valid(parentesis):
   valido = []
   for i in parentesis:
      if i == "(":
         valido += ")"
      elif i == "[":
         valido += "]"
      elif i == "{":
         valido += "}" 
      elif not valido or valido.pop() != i:
         return False
   return not valido

print(valid(parentesis))
