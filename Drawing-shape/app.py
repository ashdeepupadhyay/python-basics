from Question import Question

question_prompts = [
    "What color are apples?\na)Red\nb)Yellow\nc)Blue\n\n",
    "What color are Bananas?\na)Red\nb)Yellow\nc)Blue\n\n",
    "What color are strawberries?\na)Red\nb)Yellow\nc)Blue\n\n"
]


questions=[
    Question(question_prompts[0],"a"),
    Question(question_prompts[1],"b"),
    Question(question_prompts[2],"a"),
]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score+=1
    print("You got"+str(score)+"/"+str(len(questions))+"Correct")


run_test(questions)




