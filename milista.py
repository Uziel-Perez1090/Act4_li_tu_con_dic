# Ejemplo de uso de listas
misnovias=["Dulce", "Ana", "Lina"]
misNumeros=["666","77","10"]
# Mostrando mis novias
print(misnovias)
# Mostrando mis numeros cleros
print(misNumeros)
print("---Accediendo a Los Elementos De La Lista---")
print(misnovias[1])
if "Ana" in misnovias:
  print("si, 'Ana' esta en la lista de mis novias")
else:
  print("Que trizte No Eres Mi Niña")
print("Numero De Novias")
Nnovias = len(misnovias)
print(f"numero de novias = {Nnovias}")
print("Ciclo For En Listas")
posicion=0
for medianaranja in misnovias:
  print(posicion, " " ,medianaranja)
  posicion = posicion+1
