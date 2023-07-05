#esto es la base, es necesario pq asi se genera un archivo cada vez que se corre el codigo y acabara siendo eliminado al final 
archivo ="readme.txt"
file = open(archivo,"x") # no es necesario abrir un archivo con esto, ya que si pones file=open("readme.txt","w/a") el archivo ya se creará de por si 
file.close
file = open("readme.txt","w")
texto0 = file.write("pq no se acaba ya la puta guerra, de Ucrania ")
file.close

#principaly goal
file= open("readme.txt","r")
texto= file.read()
file.close()
print(texto)

file= open("readme.txt","a") #si usas "w" remplazas el texto que tenias por el que vas a escribir ahora, si pones "a" añades tu texto al final del otro 
contenido= input ("información añadida:")
texto2= file.write(contenido)
file.close()

import os

if os.path.exists(archivo ):
    os.remove(archivo)
    print("el archivo ha sido eliminado exitosamente")
else:
    print("el archivo no existe o ya fue eliminado")

