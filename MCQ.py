from Questions import Questions

question_prompt = [
    "What color are apples?\n(a) Red/Green\n(b) puprle\n(c) Oranger\n\n",
    "What color are Banana?\n(a) Teal\n(b) Magenta\n(c) Yellow\n\n",
    "What color are strawberries?\n(a) Yellow\n(b) Red\n(c) Blue\n\n"

]

questions = [
    Questions(question_prompt[0], "a"),
    Questions(question_prompt[1], "c"),
    Questions(question_prompt[2], "b")
]


def run_test(questions):
    score = 0
    for question in questions:
        answer = input(questions.prompt)
        if answer == question.answer:
            score += 1
    print("You got " + str(score) + "/" + str(len(questions)) + " correct")


run_test(questions)
