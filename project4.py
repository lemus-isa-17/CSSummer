"""

Isabella Lemus Project 4 : Practicing Loops

Einstein Private Elementary school has three classes in
each of its 9 grades. 27 classes total, kindergarten (grade 0) - 8th grade.

The school allows parents to pay tuition over the 9 month school year.
Tuition for grade 0 (kinder.) is $90 every month.
Tuition for the other grades is $50 times the grade level every month.

Design a programming solution that outputs nine tuition payment bills
for each of the 27 classrooms. Each bill must contain the grade number (0-8)
the classroom number (1-3), the month (1-9) and the amount due.

"""

print ("Tuition Bill Statement for Einstein Private Elementary")
for g in range(0, 9):
    print ("Grade   Class   Month   Tuition")
    for c in range(1, 4):
        for m in range(1, 10):
            if g == 0:
                t = 90
            elif g != 0:
                t = g*50
            print('{0}       {1}       {2}       {3}'.format(g, c, m, t))
        print("")
    print ("")