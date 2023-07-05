#esto es la base, es necesario pq asi se genera un archivo cada vez que se corre el codigo y acabara siendo eliminado al final 
archivo ="readme.txt"
file = open(archivo,"x")
file.close()
file = open("readme.txt","w")
texto0 = file.write("pq no se acaba ya la puta guerra, de Ucrania ")
file.close()

#principaly goal
respuesta = input("Que quieres hacer con el archivo?:\n 1--> leerlo \n 2--> escribir \n 3--> eliminarlo \n") #el \n sirve para que lo que le sigue se escriba en la siguiente linea
if int(respuesta)== 1:
    file= open("readme.txt","r")
    texto= file.read()
    file.close()
    print(texto)

if int(respuesta) == 2:
    file= open("readme.txt","a") #si usas "w" remplazas el texto que tenias por el que vas a escribir ahora, si pones "a" añades tu texto al final del otro 
    contenido= input ("información añadida:")
    file.write(contenido)
    file.close()
#ns perque de primeres si intentes eliminar el archiu et dona error i et diu que esta sent utilitzat
import os
if int(respuesta) == 3:
    if os.path.exists(archivo ):
        os.remove(archivo)
        print("el archivo ha sido eliminado exitosamente")
    else:
        print("el archivo no existe o ya fue eliminado")
    

respuesta2= len(input("Quieres hacer alguna accion más?"))

while int(respuesta2) >=3:
    respuesta = input("Que quieres hacer con el archivo?:\n 1--> leerlo \n 2--> escribir \n 3--> eliminarlo \n") #el \n sirve para que lo que le sigue se escriba en la siguiente linea
    if int(respuesta)== 1:
        file= open("readme.txt","r")
        texto= file.read()
        file.close()
        print(texto)
        respuesta2= len(input("Quieres hacer alguna accion más?"))

    if int(respuesta) == 2:
        file= open("readme.txt","a") #si usas "w" remplazas el texto que tenias por el que vas a escribir ahora, si pones "a" añades tu texto al final del otro 
        contenido= input ("información añadida:")
        texto2= file.write(contenido)
        file.close()
        respuesta2= len(input("Quieres hacer alguna accion más?"))

    import os
    if int(respuesta) == 3:
        if os.path.exists(archivo ):
            os.remove(archivo)
            print("el archivo ha sido eliminado exitosamente")
            respuesta2= 0
        else:
            print("el archivo no existe o ya fue eliminado")
            respuesta2=0
            
else: 
    print("goodbye")


