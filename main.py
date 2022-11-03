def calculate_bmi(height, weight):
    print("Height = "+str(height))
    print("Weight = " + str(weight))
    bmi= weight/(height*height)
    print("BMI="+ str(round(bmi,2)))
    if bmi<18.5 :
        print("You are underweight")
    elif bmi>=18.5 and bmi <=25.0:
        print("Your weight is in the normal range")
    else:
        print("You are underweight")

calculate_bmi(weight=57, height= 1.73)