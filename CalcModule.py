## @file CalcModule.py
#  @author Brooks MacLachlan
#  @brief Provides methods for performing calculations on student data
#  @date 1/09/2019

## @brief Sorts a list of students by gpa
#  @details Accepts a list of dictionaries, each containing data for one
#           student, and sorts them in descending order of gpa.
#  @param S List of dictionaries of student data
#  @return List of dictionaries of student data sorted by gpa
def sort(S):
    sortedStudents = sorted(S, key=lambda student: student["gpa"], 
        reverse=True)
    return sortedStudents

## @brief Computes the average gpa of male and female students
#  @details Accepts a list of dictionaries, each containing data for one
#           student, and computes the average gpa of all students whose gender
#           correspond to the gender given by the string argument
#  @param L List of dictionaries of student data
#  @param g String representing gender, either 'male' or 'female'
#  @return Float representing the average gpa of male or female students
def average(L, g):
    genderGpas = [student["gpa"] for student in L if student["gender"] == g]
    averageGpa = sum(genderGpas) / float(len(genderGpas))
    return averageGpa

## @brief Allocates students to an engineering program
#  @details Allocates students with free choice to their first choice.
#           Allocates other students, in the order of descending gpa, to their 
#           first choice if the department capacity has not been reached. If
#           their first choice is full, the student will be allocated to their
#           second choice. If their second choice is also full, the student
#           will be allocated to their third choice. Students with a gpa of 4.0
#           or lower will not be allocated.
#  @param S List of dictionaries of student data
#  @param F List of macids of students with free choice
#  @param C Dictionary of engineering department capacities
#  @return Dictionary of departments and the students allocated to them
def allocate(S, F, C):
    allocatedDict = {
        "civil": [],
        "chemical": [],
        "electrical": [],
        "mechanical": [],
        "software": [],
        "materials": [],
        "engphys": [],
    }
    allMacIds = [student["macid"] for student in S]
    for macId in F:
        currentStudent = S[allMacIds.index(macId)]
        if currentStudent["gpa"] > 4.0:
            allocatedDict[currentStudent["choices"][0]].append(currentStudent)
    remainingStudents = [student for student in S if student["macid"] not in F]
    remainingSorted = sort(remainingStudents)
    for student in remainingSorted:
        if student["gpa"] > 4.0:
            firstChoice = student["choices"][0]
            if C[firstChoice] > len(allocatedDict[firstChoice]):
                allocatedDict[firstChoice].append(student)
                continue
            secondChoice = student["choices"][1]
            if C[secondChoice] > len(allocatedDict[secondChoice]):
                allocatedDict[secondChoice].append(student)
                continue
            thirdChoice = student["choices"][2]
            if C[thirdChoice] > len(allocatedDict[thirdChoice]):
                allocatedDict[thirdChoice].append(student)
    return allocatedDict
