print ("\nA continuación se le haran un conjunto de preguntas con respuesta de eleccion múltiple, porfavor responda poniendo: a,b,c,d\n")
#pregunta 1 
file = open("archivo.txt","w")
file.write("Pregunta 1: Quien marco el gol que le dio el mundial a Espana en el 2010? \n a: David Villa \n b: Messi \n c: Iniesta \n d: Mariano Rajoy")
file.close()

file = open("archivo.txt","r")
contenido= file.read()
print( contenido)
file.close()

respuesta=input("Respuesta:")

if respuesta == "c":
    print("correcto \n")

else:
    print("incorrecto \n")

file = open("archivo.txt","a")
file.write("\n Tu respuesta ha sido: "+ respuesta + "\n\n")
file.close
#archivo final con todos los datos
file = open("archivo.txt","r")
p1=file.read()
file.close()

final_file=open("JSON.txt","w")
final_file.write(p1)
final_file.close()

file2=open("archivo2.txt","w")
file2.write("Pregunta 2: Sabe usted que es lo que quiero? \n a: La 33 \n b: La tarjeta del hormiguero \n c: La tarifa plana de Jazztel \n d: una tortilla de patatas")
file2.close()

file2=open("archivo2.txt","r")
contenido=file2.read()
print(contenido)
file2.close()

respuesta2=input("Respuesta:")

if respuesta2 == "b":
    print("correcto \n")
else:
    print("incorrecto \n")

file2 = open("archivo2.txt","a")
file2.write("\n Tu respuesta ha sido: " + respuesta2 + "\n\n")
file2.close()

file2 = open( "archivo2.txt", "r")
p2=file2.read()
file2.close()

final_file = open( "JSON.txt","a")
final_file.write(p2)
final_file.close()

file3= open("archivo3.txt","w")
file3.write("Completa la letra de la cancion: Un dia de partit,_______________, nomes entrar a la grada \n a:coty x coty \n b:jo t'espero com si res al mateix lloc de cada any \n c: ala madrid \n d: al Camp Nou vaig anar")
file3.close() 

file3=open("archivo3.txt","r")
contenido = file3.read()
print(contenido)
file3.close()

respuesta3= input("Respuesta:")

if respuesta3 == "d":
    print("correcto \n")
else: 
    print("incorrecto \n")

file3 = open("archivo3.txt","a")
file3.write("\n Tu respuesta ha sido: " + respuesta3 + "\n\n")
file3.close()

file3 = open("archivo3.txt","r")
p3=file3.read()
file3.close()

final_file= open("JSON.txt","a")
final_file.write(p3)
final_file.close()

import os

os.remove("archivo.txt")
os.remove("archivo2.txt")
os.remove("archivo3.txt")

if respuesta == "c" and respuesta2 == "b" and respuesta3 == "d" :
    conclusion="enhorabuena, has encertado 3 de 3 "
    print(conclusion)

if respuesta == "c" and respuesta2 == "b" and respuesta3 != "d" :
    conclusion="has encertado 2 de 3"
    print(conclusion)

if respuesta == "c" and respuesta2 != "b" and respuesta3 == "d" :
    conclusion="has encertado 2 de 3"
    print(conclusion)

if respuesta != "c" and respuesta2 == "b" and respuesta3 == "d" :
    conclusion="has encertado 2 de 3"
    print(conclusion)

if respuesta == "c" and respuesta2 != "b" and respuesta3 != "d" :
    conclusion="has encertado 1 de 3"
    print(conclusion)

if respuesta != "c" and respuesta2 == "b" and respuesta3 != "d" :
    conclusion="has encertado 1 de 3"
    print(conclusion)

if respuesta != "c" and respuesta2 != "b" and respuesta3 == "d" :
    conclusion="has encertado 1 de 3"
    print(conclusion)

if respuesta != "c" and respuesta2 != "b" and respuesta3 != "d" :
    conclusion="has encertado 0 de 3"
    print(conclusion)

final_file = open( "JSON.txt","a")
final_file.write("Resultado final:"+ conclusion)







