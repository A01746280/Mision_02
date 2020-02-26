# Autor: Kathia Alejandra Cervantes López, A01746280
# Este programa muestra el nmero de mujeres, hombres y el total de alumnos inscritos

mujeres= int(input("Teclea el número de mujeres inscritas: " ))

hombres= int(input("Teclea el número de hombres inscritos: " ))

total= hombres + mujeres

print("El total de alumnos incritos es:", total)

mujeres= (mujeres*100) / total
print("El total de mujeres es %.2f" % (mujeres))

hombres= (hombres*100) / total
print("El total de hombres es %.2f" % (hombres))