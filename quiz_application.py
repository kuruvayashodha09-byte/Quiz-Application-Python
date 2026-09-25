questions = [
    {
        "question": "What is the capital of India?",
        "options": ["A. Mumbai", "B. Delhi", "C. Chennai", "D. Kolkata"],
        "answer": "B"
    },
    {
        "question": "Which language is used in this project?",
        "options": ["A. Java", "B. C", "C. Python", "D. HTML"],
        "answer": "C"
    },
    {
        "question": "How many days are there in a week?",
        "options": ["A. 5", "B. 6", "C. 7", "D. 8"],
        "answer": "C"
    },
    {
        "question": "Which keyword is used to define a function in Python?",
        "options": ["A. function", "B. def", "C. fun", "D. define"],
        "answer": "B"
    },
    {
        "question": "Which of the following is a Python data type?",
        "options": ["A. list", "B. table", "C. record", "D. character"],
        "answer": "A"
    }
]

score = 0

print("===== QUIZ APPLICATION =====")

for number, question in enumerate(questions, 1):
    print("\nQuestion", number)
    print(question["question"])

    for option in question["options"]:
        print(option)

    answer = input("Enter your answer (A/B/C/D): ").upper()

    if answer == question["answer"]:
        print("Correct!")
        score += 1
    else:
        print("Wrong answer!")

print("\n===== QUIZ RESULT =====")
print("Your Score:", score, "/", len(questions))

if score == len(questions):
    print("Excellent!")
elif score >= 3:
    print("Good job!")
else:
    print("Keep practicing!")

print("Thank you for playing!")
