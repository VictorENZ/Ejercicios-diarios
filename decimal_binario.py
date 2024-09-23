decimal= 29

def convdecimal(decimal):
  modulos=[]
  while decimal != 0:
    modulos.insert(0,decimal%2)
    decimal//=2
    
  print(modulos)

convdecimal(decimal)