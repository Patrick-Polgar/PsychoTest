""" psycho_test """

# Define the list of questions
questions = [
    "What do you think, do you know yourself good enough?",
    "Do you enjoy to speak with many people?",
    "Do you like to speak about your emotions with your friends",
    "Are you an optimist?",
    "Do you like to be in a community?",
    "Do you like to share your ideas with others?"
]

# create a list to store the answers
answers = []

# Loop through the questions and promt the user for an answer
for question in questions:
    while True:
        answer = input(question + " (yes/no) ")
        if answer in ["yes", "no"]:
            answers.append(answer)
            break
        else:
            print("Error, please type 'yes' or 'no'!")

# Analyze the answers to determine the psychology type
extravert_score = 0
for answer in answers:
    if answer == "yes":
        extravert_score += 1

if extravert_score > 2:
    psychology_type = "Extraverted"
else:
    psychology_type = "Introverted"

# It is just a basic beginner task to decide it, whether someone extraverted or introverted

# Print the results
print("Based on your answers, your psychology type is:", psychology_type)

