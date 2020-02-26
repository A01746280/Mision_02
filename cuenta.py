# Kathia Alejandra Cervantes López
#Este programa calcula el costo total de una comida en un restaurante

total = float(input("Teclea el total de la cuenta: "))

print("El total de la cuenta es: $ %.2f"  % (total))


propina= ((total*0.13) + total)

print("El total de la cuenta más IVA es: ", propina)

IVA= ((total*0.16) + total)
print("El total de la cuenta más 16% de IVA es: $" ,IVA)
 
totalneto= (propina+IVA)
print("El total de la cuenta: ", totalneto, "pesos")

