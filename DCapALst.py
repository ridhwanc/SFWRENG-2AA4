## @file DCapALst.py
# @title Department Capacity Association List
# @author Ridhwan Chowdhury
# @date February 12
from StdntAllocTypes import *


## @brief This class is called before any other access program
# @details Creates a set for departments and their respectve capacities
class DCapALst():
        ## @brief Initializes the set
        @staticmethod
        def init():
            DCapALst.s = {(DeptT, 0)}

        ## @brief Adds a deparment and it's respective capacity into the set
        # @details if the department exists in the set, raise and error
        # if not, union that set with the overarching DCapALst set
        # @param d describes the department object as a type
        # @param n represents the capacity of each object as an integer
        @staticmethod
        def add(d, n):
            a_data = {(d, n)}
            if a_data.issubset(DCapALst.s) is True:
                raise KeyError
            else:
                DCapALst.s = DCapALst.s.union(a_data)

        ## @brief Removes a department its capacity from the set
        # @details Removes a department and capacity from the set, if the department
        # doesn't exist, function raises an error
        # @param d it represents the department type
        @staticmethod
        def remove(d):
            for data in DCapALst.s:
                if d == data[0]:
                    r_data = {(data[0], data[1])}
            if r_data == {}:
                raise KeyError
            else:
                DCapALst.s = DCapALst.s.difference(r_data)

        ## @brief returns a boolean if the department exists in the set
        # @details Locates the department in the set to determine if it exists
        # if doesn't exist, returns false, if it does, returns true
        # @param d represents the department type
        @staticmethod
        def elm(d):
            for data in DCapALst.s:
                if d == data[0]:
                    p_data = set(data)
            if p_data.issubset(DCapALst.s) is True:
                return True
            else:
                return False
