import os

#file=open("file.txt","x")
#file.close()                                no es necesario
file=open("file.txt","w")
texto=input("cuentame algo: ")
file.write(texto)
file.close()
file=open("file.txt","r")
contenido=file.read()
reversed_contenido= contenido[::-1]
file.close()


#file2= open("archivo.txt","x")
#file2.close()
file2= open("archivo.txt","w")
file2.write((reversed_contenido))
file2.close()
file2= open("archivo.txt","r")
lecture=file2.read()
print(lecture)
file2.close()

os.remove("file.txt")
os.remove("archivo.txt")
