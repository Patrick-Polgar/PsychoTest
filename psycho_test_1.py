""" psycho_test """

# Define the list of questions
questions = [
    "1. What do you think, do you know yourself good enough?",
    "2. Do you enjoy to speak with many people?",
    "3. Do you like to speak about your emotions with your friends",
    "4. Are you an optimist?",
    "5. Do you like to be in a community?",
    "6. Do you like to share your ideas with others?",
    "7. Do you like to play with the children?",
    "8. Do you hate to read everyday alone?",
    "9. Do you like to walk among people on the street?",
    "10.Do you think, being alone for a long time is boring?"
]

# create a list to store the answers
answers = []

# Loop through the questions and promt the user for an answer 
# By typo get an error message
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

psychology_type = ""
if extravert_score >= 8:
    psychology_type = "Strong Extraverted"
elif extravert_score >= 6:
    psychology_type = "Light Extraverted"
elif extravert_score == 5:
    psychology_type = "Balanced"
elif extravert_score >= 3:
    psychology_type = "Light Introverted"
else:
    psychology_type = "Strong Introverted"

# Print the results
print("Based on your answers, your character is:", psychology_type)