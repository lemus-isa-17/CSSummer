"""
Isabella Lemus - Project 6

Create a program to produce a Grade Point Total and Average Report
as shown on the printer spacing chart.

This reports each student's course grade and calculated grade point total for the 
first two courses a student takes. The report is to print 20 detail lines 
per page with headings & page numbers on each page.

You will also need to select certain records to print.

Design and write the program following the specifications below.

INPUT(Record Layout): Your data file (GradePtsFile.txt)

Do not proces records where the grade for either course is 0.0

For each student whose record is processed calculate:
Earned Grade Points for each course as the product of credit hours and grade
Student's GPA for the two courses (Sum of Grade Points / Sum of Credit Hours)

Accumulate three Final Totals to print at the end of the report (and use for averages)
Total Number of Students
Total Credit Hours
Total Earned Grade Points

At End of File, calculate Overall Grade Point Average (Total Earned Grade Points / Total Credit Hours)

"""

import csv
import math
import os

pageNum = 1

# Function to print page header, pg is page number
def printPageHeader(pg):
    print ("STUDENT GRADE POINT REPORT".center(100), end='')
    print ("Page: ".rjust(10) + str(pageNum))
    print ("By: Isabella Lemus".center(100))
    print ()

# Function to print column header
def printColumnHeaders():
    print ("Student".ljust(15), end = '')
    print ("CourseID One".ljust(16), end = '')
    print ("Cr.".ljust(11), end = '')
    print ("Grade".ljust(11), end = '')
    print ("Grade Pts".ljust(15), end='')
    print ("CourseID Two".ljust(16), end = '')
    print ("Cr.".ljust(11), end = '')
    print ("Grade".ljust(11), end = '')
    print ("Grade Pts".ljust(15), end='')
    print ("GPA".ljust(4), end = '')
    print ()

# Function to calculate earned grade points, round to one dec and return
# num1 is credit hours, num2 is grade
def calcEarnedGradePoints(num1, num2):
    return round(num1 * num2, 1)

# Function to caluclate student's GPA for two courses, round to two dec and return
# num1 is Sum of Grade Points, num2 is Sum of Credit Hours
def calcGradePointAvg(num1, num2):
    return round(num1 / num2, 2)

# Function to print totals
def printTotals(st, ch, egp, gpa):
    print ("\nFINAL TOTALS: ")
    print ("\tTotal Number of Students: " + str(st))
    print ("\tTotal of all Credit Hours: " + str(ch))
    print ("\tTotal of all Earned Grade Points: " + str(egp))
    print ("\tFinal Grade Point Average: " + str(gpa))
    print ()

printPageHeader(pageNum)
printColumnHeaders()

totalStudents = 0
totalCreditHours = 0
totalEarnedGPs = 0
finalGPA = 0

# Open file to read
f = open('GradePointFile.txt', 'r')

# Check if file is opened
if f.mode == 'r':
    # Go through each row of data in file
    for row in csv.reader(f):

        if not row:
            continue

        studentName = row[0]
        crOneID = row[1]
        crOneCreditHours = float(row[2])
        crOneGrade = float(row[3])
        crTwoID = row[4]
        crTwoCreditHours = float(row[5])
        crTwoGrade = float(row[6])

        if crOneGrade == 0.0 or crTwoGrade == 0.0:
            continue
            
        egp1 = calcEarnedGradePoints(crOneCreditHours, crOneGrade)
        egp2 = calcEarnedGradePoints(crTwoCreditHours, crTwoGrade)

        sumEgp = egp1 + egp2
        sumCH = crOneCreditHours + crTwoCreditHours
        studentGPA = calcGradePointAvg(sumEgp, sumCH)

        # Output to console
        print (studentName.ljust(15), end = '')
        print (crOneID.ljust(16), end = '')
        print (str(egp1).ljust(11), end = '')
        print (str(crOneCreditHours).ljust(11), end = '')
        print (str(crOneGrade).ljust(15), end = '')
        print (crTwoID.ljust(16), end = '')
        print (str(crTwoCreditHours).ljust(11), end = '')
        print (str(crTwoGrade).ljust(11), end = '')
        print (str(egp2).ljust(15), end = '')
        print (str(studentGPA).ljust(4), end = '')
        print ()

        totalStudents += 1
        totalCreditHours += sumCH
        totalEarnedGPs += sumEgp

        if totalStudents % 20 == 0:
            pageNum += 1
            print ()
            printPageHeader(pageNum)
            printColumnHeaders()


finalGPA = calcGradePointAvg(totalEarnedGPs, totalCreditHours)

# Print out final numbers
printTotals(totalStudents,totalCreditHours,totalEarnedGPs,finalGPA)
