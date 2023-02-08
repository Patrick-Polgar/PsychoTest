""" calculate_result """ 

def calculate_result(answers):
    extravert_score = 0
    for i in range(0, 10):
        if answers.get(str(i)) == "yes":
            extravert_score += 1
            # elif answers.get(str(i)) == "no":
            # extravert_score -= 1

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
