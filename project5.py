"""

Isabella Lemus - Project 5

Create a programming solution for an elementray school that has 
24 classes : 3 classes for each grade, grades 1 - 8.

Each classroom has anywhere between 25 and 35 students.
Each student is assigned a random student ID of 3 letters and 3 numbers.
Have the computer program randomly generate the student ID.

Each student takes an achievement test at the end of the year.
The scores range from zero to 100. 
Have the computer program create the scores randomly for the students.

In your output, show the scores for each of the students, the 
classroom average score, the average score for each grade level, and the 
average score for the school.

"""

import random

print("\n\n\n")

letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
            "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]


#counters
classCounter = 0; gradeCounter = 0; schoolCounter = 0

#accumulators
classTotal = 0; gradeTotal = 0; schoolTotal = 0

grade  = 0

for grade in range (1,9):
    print ("\n ------- GRADE " + str(grade) + "-------")

    gradeCounter = 0
    gradeTotal = 0

    for cl in range (1,4):

        clSize = random.randint(25,35)
        classCounter = 0
        classTotal = 0

        print ("\n --- GRADE: " + str(grade) + ", CLASS : " + str(cl) + ", SIZE : " + str(clSize) + " ---")
        for student in range(clSize):
            id = ""
            for letter in range(0,3):
                id += letters[random.randint(0,25)]
            id += str(random.randint(100,999))

            score = random.randint(0,100)
            print(" Student " + str(student + 1) + " : " + id + ",   Score : " + str(score))
            
            classCounter += 1
            gradeCounter += 1
            schoolCounter += 1
            

            classTotal += score
            gradeTotal += score
            schoolTotal += score

        print ("\nCLASS AVERAGE : " + "{:.2F}".format(classTotal/classCounter))
    print ("\nGRADE AVERAGE : " + "{:.2F}".format(gradeTotal/gradeCounter))
print ("\nSCHOOL AVERAGE : " + "{:.2F}".format(schoolTotal/schoolCounter))
print("")
