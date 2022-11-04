def calculate_bmi(height, weight):
    print("Height = "+str(height))
    print("Weight = " + str(weight))
    bmi= weight/(height*height)
    print("BMI="+ str(round(bmi,2)))
    if bmi<18.5 :
        # print("You are underweight")
        return -1
    elif bmi>=18.5 and bmi <=25.0:
        # print("Your weight is in the normal range")
        return 0
    else:
        # print("You are underweight")
        return 1

calculate_bmi(weight=57, height= 1.73)