""" calculate_result """ 

def calculate_result(answers):
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
    return psychology_type
