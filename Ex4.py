def main():
    q = get_user_input()
    calc_average_temperature(q)
    calc_min_max_temperature(q)
    calc_median_temperature(q)

def get_user_input():
    # creating an empty list
    numbers = []
    # number of elements as input
    n = int(input("Enter number of elements : "))

    # iterating till the range
    for i in range(0, n):
        ele = int(input())

        numbers.append(ele)  # adding the element
    print(numbers)
    return numbers

def calc_average_temperature(q):
    numbers = q
    sum = 0.0
    for i in range(0, len(numbers)):
        sum+=numbers[i]

    average = sum/len(numbers)
    print("The average is "+ str(average))
    return average

def calc_min_max_temperature(q):
    minval = q[0]
    maxval = q[0]
    for i in q:
        if i < minval:
            minval = i
        if i > maxval:
            maxval = i
    print("The minimum value is "+ str(minval))
    print("The maximum value is "+str(maxval))
    return [minval,maxval]


def calc_median_temperature(q):
    size = len(q)
    if (size%2==1):
        location1 = int(size / 2)
        median_value=q[location1]
        print("The value in the middle is " + str(median_value))
    else:
        location2 = int((size / 2)-1)
        median_value = q[location2]+0.5
        print("The value in the middle is " + str(median_value))

    return median_value
if __name__ == "__main__":
    main()