#!/usr/bin/env python
dni=input("Escribe tú número de DNI con la letra \n", )
print(dni[:-1])
resto=int(str(dni[:-1]))%23
letra=""
lista1=list(range(23))
lista2=["T", "R", "W", "A", "G", "M", "Y", "F", "P", "D", "X", "B", "N", "J", "Z", "S", "Q", "V", "H", "L", "C", "K", "E"]
if resto in lista1:
	letra=lista2[lista1.index(resto)]
	print ("DNI correcto")
if dni[-1]!=letra:
	print ("El DNI no es correcto")

correo=input("Escribe tú correo \n", )
variable=0
while variable:
	for char in correo:
		if char=="@":
			variable=1
		if variable==1 and char==".":
			variable=2
		if variable==2 and (char!="." and char!="@"):
			variable=3
		if variable==3:
			print ("correo correcto")
			break;
		print("correo incorrecto")
		break;