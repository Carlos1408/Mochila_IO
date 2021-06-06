cantidad=4
capacidad=33
# import src.ingreso_datos
# articulo
# peso
# utilidad


# item=[]
# item.append([cantidad,capacidad])
# item.append(['Aceite', 1, 8])
# item.append(['Azucar', 3, 7])
# item.append(['Maiz', 2, 7])
# item.append(['Frijol', 2, 9])
item=[cantidad,capacidad]
a=['Aceite', 1, 8]
b=['Azucar', 3, 7]
c=['Maiz', 2, 7]
d=['Frijol', 2, 9]


fic = open("text_1.txt", "w")
fic.write(str(item))   
fic.write(str(a))
fic.write(str(b))
fic.write(str(c))
fic.write(str(d))
fic.close()


# fic = open('text_1.txt', "r")
# # lines = list(fic)
# lines = []
# for line in fic:
#     lines.append(line)
# print(lines)
# fic.close()