## @file DCapALst.py
# @title Student Association List
# @author Ridhwan Chowdhury
# @date February 12
from StdntAllocTypes import *
from DCapALst import *
from AALst import *


## @brief This class is called before any other access program
# @details Creates a set for departments and their respective capacities
class SALst():
        ## @brief Initializes the set with student macids
        @staticmethod
        def init():
            SALst.s = {(StudentT, 0)}

        ## @brief Adds a student's macid into the set
        # @param m describes student macid
        # @param i represents student info
        @staticmethod
        def add(m, i):
            a_data = {(m, i)}
            if a_data.issubset(SALst.s) is True:
                raise KeyError
            else:
                DCapALst.s = SALst.s.union(a_data)

        ## @brief Removes a student information from set
        # @param m it represents the student type
        @staticmethod
        def remove(m):
            for data in SALst.s:
                if m == data[0]:
                    r_data = {(data[0], data[1])}
            if r_data == {}:
                raise KeyError
            else:
                DCapALst.s = SALst.s.difference(r_data)

        ## @brief returns a boolean if the student exists in the set
        # if doesn't exist, returns false, if it does, returns true
        # @param m represents the student type
        @staticmethod
        def elm(m):
            for data in SALst.s:
                if m == data[0]:
                    p_data = set(data)
            if p_data.issubset(ALst.s) is True:
                return True
            else:
                return False

        ## @brief A program that detects student string and outputs student info
        # @param m The parameter represents student macid
        # @return Returns fname lname..etc
        @staticmethod
        def info(m):
            for data in SALst.s:
                if m == data[0]:
                    if m.issubset(SALst.s) is True:
                        return data[1]
                    else:
                        raise KeyError

        ## @brief A program that outputs string and sorts student info by gpa
        # @param f list of students with their respective information
        # @return Returns a sequence of strings
        @staticmethod
        def sort(f):
            num_max = 0
            temp_1 = -1
            lst = []

            f_func = []
            for i in SALst.s:
                if f == i[1]:
                    f_func.append(i)
            for i in range(len(f_func)):
                for j in range(i, len(f_func)):
                    if (f_func[j])[1].gpa > num_max:
                        num_max = (f_func[j])[1].gpa
                        temp_1 = j
                temp_2 = f_func[i]
                f_func[i] = f_func[temp_1]
                f_func[temp_1] = temp_2
                num_max = 0
            for i in f_func:
                lst.append(i[0])
            return lst

        ## @brief A program that outputs string and sorts student info by gpa
        # @param f list of students with their respective information
        # @return Returns a real number
        @staticmethod
        def average(f):
            avg = float(0)
            set_f = []
            for i in SALst.s:
                if f == i[1]:
                    set_f.append(i)
            if len(set_f) == 0:
                raise ValueError
            for i in set_f:
                avg = avg + i[1].gpa

        ## @brief allocates students into their respective programs
        @staticmethod
        def allocate():
            AALst.init()
            f = SALst.sort(lambda x: x.freechoice and (x.gpa >= 4.0))
            for m in f:
                choose = SALst.info(m).choices
                AALst.add_stdnt(choose.next(), m)
            s = SALst.sort(lambda x: not x.freechoice and (x.gpa >= 4.0))
            for m in s:
                choose = SALst.info(m).choices
                alloc = False

                while not alloc and not ch.end():
                    d = choose.next()
                    if AALst.num_alloc(d) < DCapALst.capacity(d):
                        AALst.add_stdnt(d, m)
                        alloc = True
                if not alloc:
                    raise RuntimeError
