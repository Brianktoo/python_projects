#!/usr/bin/env python

score = float(input('please enter the marks (0-100):'))

if 0 <= score <= 100:
    if score < 60:
        grade ='E'
    elif score >= 60 and  score < 70:
        grade ='D'
    elif score >= 70 and score <80:
        grade ='C'
    elif score >= 80 and score <90:
        grade ='B'
    elif score >= 90:
        grade = 'A'
    print('grade', grade)
else:
     print('Invalid score, Enter a score between value 0-100')          
            

