def bmi(weight, height):
    your_bmi = weight / (height*height)
    if your_bmi <= 18.5:
        return "Underweight"

    elif your_bmi <= 25.0:
        return "Normal"

    elif your_bmi <= 30.0:
        return "Overweight"

    else:
        return "Obese"

