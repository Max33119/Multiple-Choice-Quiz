from Class import Question

question_prompts = [
"What year did the original Air jordan one come out?\n(a) 1990\n(b) 1985\n(c) 1987\n\n",
"How many NBA championship titles does Micheal jordan have?\n(a) 3\n(b) 8\n(c) 6\n\n",
"What Jordan sneaker has a list of MJs achievments on the sole?\n(a) 8\n(b) 3\n(c) 10\n\n"
]

questions = [
    Question(question_prompts[0], "b"),
    Question(question_prompts[1], "c"),
    Question(question_prompts[2], "c"),
]

def run_quiz(questions):
    score = 0
    for question in questions:
        Answer = input(question.Question)
        if Answer == question.Answer:
            score += 1
    print("you got " + str(score) + "/" + str(len(questions)) + " correct")

run_quiz(questions)

input("\npress enter to end quiz")