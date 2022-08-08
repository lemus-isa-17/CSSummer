"""
Isabella Lemus Project 3B

Write a programming solution that will get a student's grade
expressed as a whole number (int) between 0 and 100
inclusive.

If the student scored >= 85, say "Excellent work! A
score of ___ is an excellent grade. Great job!"

If the student scored between 70 and 85 tell them "You
scored ___. This is a respectable grade."

If the score is <= 70, tell them "You only scored ___.
You might want to try harder next time."

Test the application with multiple different inputs.
"""

grade = int(input("Enter your grade as a whole number: "))

if grade >= 85:
    print ('Excellent work! A score of {} is a great grade.'.format(grade))
    print ('Good job!')
elif grade > 70:
    print ('You scored {}. This is a respectable grade.'.format(grade))
else:
    print ('You only scored {}. You may want to try harder next time.'.format(grade))
