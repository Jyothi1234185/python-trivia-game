#list of questions
#store the answers
#randomly pick questions
#ask questions
#check if the answer is correct
#keep track of score
#tell the user their score at the end

import random
questions={
    "What is the keyword to define a function in Python?": "def",
    "What data type is used to store true/false values in Python?": "bool",
    "Which built-in function is used to get the length of a string or list?": "len",
    "What symbol is used to comment a single line in Python?": "#",
    "What is the output of 3 + 2 * 2 in Python?": "7",
    "What keyword is used to create a class in Python?": "class",
    "Which module in Python is used for regular expressions?": "re",
    "What is the method to add an item to the end of a list in Python?": "append",
    "What is the file extension for Python files?": ".py",
    "Which keyword is used to handle exceptions in Python?": "try",
    "What is the name of the Python package manager?": "pip",
    "What does the 'len()' function return when called on a string?": "length of the string",
    "What is the output of the expression '5 // 2' in Python?": "2",
    "Which keyword is used to define a generator function in Python?": "yield",
    "What is the purpose of the 'self' parameter in Python class methods?": "to refer to the instance of the class",
    "How do you create a virtual environment in Python?": "venv",
    "What is the output of the expression 'bool(0)' in Python?": "False",
    "Which built-in function is used to convert a string to an integer in Python?": "int",
    "What is the method to remove an item from a list by value in Python?": "remove",
    "What keyword is used to import modules in Python?":"import",


}
def trivia_game():
    question_list=list(questions.keys())
    total_questions=10
    score=0
    selected_questions=random.sample(question_list,total_questions)
    for idx,question in enumerate(selected_questions):
        print(f"{idx+1}:{question}")
        user_answer=input("Your answer: ").lower().strip()
        correct_answer=questions[question]
        if user_answer==correct_answer.lower():
            print("Correct!\n")
            score+=1
        else:
            print(f"Wrong! The correct answer is: {correct_answer}\n")
    print(f"Your final score is {score} out of {total_questions}")
    if(score==total_questions):
        print("Excellent! You got a perfect score!")
    elif(score>=7 and score<10):
        print("Great job! You have a good understanding of Python.")
    elif(score>=4 and score<7):
        print("Not bad, but there's room for improvement.")
    else:
        print("Keep practicing! You'll get better with more study.")
    
trivia_game()