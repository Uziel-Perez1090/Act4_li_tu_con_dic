arcoiris=("azul", "verde", "rojo", "amarillo")
print(arcoiris)
print("-longitud arcoiris-")
print(len(arcoiris))
animales=("Pantera", 20, "Estatura", 1, 7)
print(animales)
print("elementos de la tupla")
print(animales[2])
rateros=("juan","ana","pedro")
y = list(rateros)
y[0] = "polainas"
x = tuple(y)
print(x)
print("Agregando Elementos")
Nanimal = ("boby", "chetos")
y = list(Nanimal)
y.append("tontolin")
otratupla = tuple(y)
print(otratupla)
print("Uso De For En Tuplas")
for elcolor in arcoiris:
    print(elcolor)
    

