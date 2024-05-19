print("hello User")
playing = input("Do you want to play? :")

if  playing.lower() != 'yes':
    quit()

user = input("Enter your name : ")
print("Hello", user, " I have some questions for you")
questions = ["What is the capital city of Kenya? :", "When did Kenya get Independence: ", "When was King Pepela Born? ", "When is Today? :"]
answers = []
correctanswers = ["Nairobi", "1963", "1999", "Tuesday"]
for question in questions:
    answer = input(question)
    answers.append(answer)

i=0
result = 0
for userAnswer in answers:
    if userAnswer.lower() == correctanswers[i].lower():
        result += 1
    if userAnswer.lower() != correctanswers[i].lower():
        result +=0
    i+=1

 

print("Your score is :",str(int((result/len(questions)) * 100))+"%")