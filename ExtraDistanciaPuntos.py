#Kathia Alejandra Cervantes López
#Este programa calcula la distancia entre dos puntos

X1= int(input("Teclea la cordenada X1: "))
Y1= int(input("Teclea la cordenada Y1: "))
X2= int(input("Teclea la cordenada X2: "))
Y2= int(input("Teclea la cordenada Y2: "))

puntos= ((X2 - X1)**2 + (Y2 - Y1)**2)
print("La distancia entre los puntos es la raiz de: ", puntos)