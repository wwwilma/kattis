# Defining the function, with parameters people (number of people) and grades.
def above_average(people, grades):
    sum = 0 # initialize variable called sum
    for grade in grades:
        sum += grade

    average = sum / people # how to calculate the average 
    peopleAboveAverage = 0 # initialize variable called peopleAboveAverage
    for grade in grades:
        if average < grade: 
            peopleAboveAverage += 1 # value inside peopleAboveAverage increments with 1 if grade is above average 

    percentageAboveAverage = peopleAboveAverage / people * 100 # calculating the precentage
    print("{:.3f}%".format(percentageAboveAverage)) # printing precentage into required format


tests = int(input())
for test in range(tests):
    people, * grades = list(map(int, input().split())) 
    above_average(people, grades)