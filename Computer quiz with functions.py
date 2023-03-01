#question and correct_answer are the arguments to the function
#return is giving me some output
def ask_question(question, correct_answer):
    answer = input(question)
    if answer.lower() == correct_answer:
        print ("Your answer is correct")
        return 1
    else:
        print ("Your answer is incorrect")
        return 0
score=0
score += ask_question ("what does cpu stand for? ", "central processing unit")
score += ask_question ("what is ram? ", "random access memory")
score += ask_question ("what is port 53 used for? ", "dns")
score += ask_question ("what is rom? ", "read only memory")
print("You got " + str(score) + " questions correct!")
print("You got " + str((score/4) * 100) + "%")
