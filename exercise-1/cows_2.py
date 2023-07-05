#principal goal 
import random 
question1= "how many cows are in Girona?"
question2= "How many cows are?"
question3= "How many cows are here?"
question4= "Como que 33"
question5= "Hay 4 vacas"
question6= "vaca"
question7= "vacas"
question8= "muchas vacas"
question9= "una vaca"
question10="no hay vacas"

lista_questions=[question1,question2,question3,question4,question5,question6,question7,question8,question9,question10]
question_aleatoria= random.choice(lista_questions)
print(question_aleatoria)
respuesta= int( input("cuantas vacas hay?"))
if len(question_aleatoria.split()) == respuesta:
    print( "lo has clavado")
else:
    print( "fallastes")
final_question= input("quieres volver a jugar?")
respuesta_final=len((final_question))
while respuesta_final >= 3:
    question_aleatoria= random.choice(lista_questions)
    print(question_aleatoria)
    respuesta= int( input("cuantas vacas hay?"))
    if len(question_aleatoria.split()) == respuesta:
        print( "lo has clavado")
    else:
        print( "fallastes")

    final_question= input("quieres volver a jugar?")
    respuesta_final=len(final_question)
else:
    print("goodbye")


   


