## @file CalcModule.py
#  @Ridhwan Chowdhury, 400075426
#  @This module takes our ReadAllocationData module and now manipulates to sort, average and allocate students into their respective departments 
#  @January 19th 2019

from ReadAllocationData import readStdnts, readFreeChoice, readDeptCapacity

def sort(S):
#    took a list of dictionaries, used a sorted function with the key lambda to sort in ascending order, and then used a reverse boolean to make it in descending order
    sort_dict = sorted(S, key=lambda k: k['gpa'], reverse=True)
    
    return sort_dict

sort(readStdnts('readstudents.txt'))

def average(L, g):
    
#    intialized the gpa and count for each student, if it met the conditions, it would create a count and accumulate gpa for it to be averaged at the end of the loop

    gpa = 0
    count = 0
    for i in L:
        if i['gender'] == g:
            gpa = gpa + i['gpa']
            count = count + 1
    avg_gpa = gpa/count
    
    return avg_gpa

average(readStdnts('readstudents.txt'),'Male')

def allocate(S, F, C):
    
#    initialized dictionary for each department and an empty list that would contain list of student dictionaries

    enroll_dict = { 'civil': [], 'chemical': [], 'electrical': [], 'mechanical': [], 'software': [], 'materials': [], 'engphys': [] }
    for student in S:
        
#        determines students with gpa below 4.0, removes them from list of dictionaries

        if student['gpa'] < 4.0:
            S.remove(student)
        else:
            
#            determines students with free choice, allocates them into their respective first choice department, removes them from the list of dictionaries

            if student['macid'] in F:
                enroll_dict[student['choices'][0]].append(student)
                C[student['choices'][0]] -= 1
                S.remove(student)

    for student in S:
        
#        looks at the remaining students that do not have free choice, and are above a 4.0 gpa, and allocates to respective department based on higher GPA

        if C[student['choices'][0]] > 0:
            enroll_dict[student['choices'][0]].append(student)
            S.remove(student)
            C[student['choices'][0]] -= 1
        elif C[student['choices'][1]] > 0:
            enroll_dict[student['choices'][1]].append(student)
            S.remove(student)
            C[student['choices'][1]] -= 1
        else:
            enroll_dict[student['choices'][2]].append(student)
            S.remove(student)
            C[student['choices'][2]] -= 1
    
    return enroll_dict


allocate(readStdnts('readstudents.txt'), readFreeChoice('freechoice.txt'), readDeptCapacity('departments.txt'))
