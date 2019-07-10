## @file AALst.py
#  @author S. Smith, M. Niazi
#  @brief Module that creates the student-department allocation association.
#  @date Jan 28, 2019
#  @details Assumes init is called before any other access program.

from StdntAllocTypes import *


## @brief An abstract data type for storing department allocations
class AALst:

    s = {}

    ## @brief init initial data structure
    @staticmethod
    def init():
        for d in DeptT:
            AALst.s.update({d: []})

    ## @brief Adds student to list of students allocated to certain department
    #  @param d department type to add student m to
    #  @param m string identifying student allocated to department d
    @staticmethod
    def add_stdnt(d, m):
        AALst.s[d].append(m)

    ## @brief Obtains list of students allocated to a certain department
    #  @param d the department for which list of students should be returned
    #  @return list of allocated students to department d
    @staticmethod
    def lst_alloc(d):
        return AALst.s.get(d)

    ## @brief Obtains the number of students allocated to a certain department
    #  @param d the department for which number of students should be counted
    #  @return number of allocated students to department d
    @staticmethod
    def num_alloc(d):
        return len(AALst.s.get(d))
