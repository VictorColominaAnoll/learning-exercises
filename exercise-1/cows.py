#principal goal 

question1= input( "ask me a question: " )
#cows=len(question1.split())
cows=(question1.count(" "))
#print("the answear is: {}" .format (cows)) 
#print("the ansewar is : {cows}")
print("the answear is", cows)

#secondary goal
question2= input( "do you want to play again? ")
restart= len(question2)

while restart >= 3:
    question1= input( "ask me a question: " )
    cows=len(question1.split())
    print("the answear is", cows)
    question2= input( "do you want to play again? ")
    restart= len(question2)
else:
    print("goodbye")

   


