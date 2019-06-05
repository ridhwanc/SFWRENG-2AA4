# @file ReadAllocationData.py
#  @Ridhwan Chowdhury, 400075426
#  @This module defines several functions that retrives student information in the form of a list of dictionaries, determines a list of students with free choice, and determining department capacity in key and value pairs
#  @January 18th 2019

def readStdnts(s):
#    this is to initialize my list and dictionary in order to append each key and value line by line

    my_dict = {'macid': ' ', 'fname': ' ', 'lname': ' ','gender': ' ', 'gpa': ' ', 'choices': []}
    my_list = ['macid', 'fname', 'lname', 'gender', 'gpa', 'choices']
    true_list = []
    x = open(s, 'r')
    
#    iterate every line, split strings and values and append them into the correct index in my true_list of dictionaries

    for lines in x:
        a = lines.split()
        a[4] = float(a[4])
        index = 0
        pick1 = a[-3]
        pick2 = a[-2]
        pick3 = a[-1]
        del a[-3]
        del a[-2]
        del a[-1]
        picklist = []
        picklist.append(pick1)
        picklist.append(pick2)
        picklist.append(pick3)
        for i in a:
            my_dict[(my_list[index])] = a[index]
            index = index + 1
        
        my_dict['choices'] = picklist

        true_list.append(dict(my_dict))

    
    return true_list

readStdnts('readstudents.txt')

def readFreeChoice(s):
    
#    initialize my list where students with free choice will be appended to

    true_list = []
    x = open(s, 'r')
    for lines in x:
        a = lines.split()
        
#        students with yes beside their name in the text file are considered to be in free choice, based on if statement , if yes - they're appended into free choice list

        if a[1] == 'Yes':
            true_list.append(a[0])

    
    return true_list

readFreeChoice('freechoice.txt')


def readDeptCapacity(s):
    
#    the text file includes the name of the department along with a value that represents their capacity split by a single space

    my_dict = {}
    x = open(s, 'r')
    for lines in x:
        a = lines.split()
        department = a[0]
        capacity = a[1]
        newcapacity = int(capacity)
        my_dict[department] = newcapacity


    return my_dict

readDeptCapacity('departments.txt')




