## @file test_Calc.py
#  @author Brooks MacLachlan
#  @brief Test cases for CalcModule.py 
#  @date 1/09/2019

import pytest
from CalcModule import sort, average, allocate

student1 = {
    "macid": "student1",
    "fname": "Student",
    "lname": "One",
    "gender": "female",
    "gpa": 7.0,
    "choices": ["chemical", "software", "civil"],
}
student2 = {
    "macid": "student2",
    "fname": "Student",
    "lname": "Two",
    "gender": "female",
    "gpa": 12.0,
    "choices": ["chemical", "materials", "engphys"],
}
student3 = {
    "macid": "student3",
    "fname": "Student",
    "lname": "Three",
    "gender": "male",
    "gpa": 3.0,
    "choices": ["software", "electrical", "civil"],
}
student4 = {
    "macid": "student4",
    "fname": "Student",
    "lname": "Four",
    "gender": "male",
    "gpa": 5.0,
    "choices": ["chemical", "software", "materials"],
}
student6 = {
    "macid": "student6",
    "fname": "Student",
    "lname": "Six",
    "gender": "male",
    "gpa": 10.0,
    "choices": ["chemical", "software", "engphys"],
}
student8 = {
    "macid": "student8",
    "fname": "Student",
    "lname": "Eight",
    "gender": "female",
    "gpa": 2.0,
    "choices": ["chemical", "software", "engphys"],
}

testStudents = [student1, student2, student3, student4, student6, student8]

testCapacities = {
    "civil": 35,
    "chemical": 2,
    "electrical": 100,
    "mechanical": 46,
    "software": 1,
    "materials": 23,
    "engphys": 11,
}

testFreeStudents = ["student4", "student8"]

allocatedStudents = allocate(testStudents, testFreeStudents, testCapacities)

def test_sort():
    expectedSort = [student2, student6, student1, student4, student3, student8]
    assert sort(testStudents) == expectedSort

def test_average_male():
    expectedAvg = pytest.approx(6.0)
    assert average(testStudents, "male") == expectedAvg

def test_average_female():
    expectedAvg = pytest.approx(7.0)
    assert average(testStudents, "female") == expectedAvg

def test_allocate_correct_size():
    expectedNumAllocatedStudents = 4
    numAllocatedStudents = (len(allocatedStudents["civil"])
                            + len(allocatedStudents["chemical"])
                            + len(allocatedStudents["electrical"])
                            + len(allocatedStudents["mechanical"])
                            + len(allocatedStudents["software"])
                            + len(allocatedStudents["materials"])
                            + len(allocatedStudents["engphys"]))
    assert numAllocatedStudents == expectedNumAllocatedStudents

def test_allocate_less_than_four_gpa_unallocated_free():
    assert (student8 not in allocatedStudents["civil"]
            and student8 not in allocatedStudents["chemical"]
            and student8 not in allocatedStudents["electrical"]
            and student8 not in allocatedStudents["mechanical"]
            and student8 not in allocatedStudents["software"]
            and student8 not in allocatedStudents["materials"]
            and student8 not in allocatedStudents["engphys"])

def test_allocate_less_than_four_gpa_unallocated_not_free():
    assert (student3 not in allocatedStudents["civil"]
            and student8 not in allocatedStudents["chemical"]
            and student3 not in allocatedStudents["electrical"]
            and student8 not in allocatedStudents["mechanical"]
            and student8 not in allocatedStudents["software"]
            and student8 not in allocatedStudents["materials"]
            and student3 not in allocatedStudents["engphys"])

def test_allocate_free_choice():
    assert student4 in allocatedStudents["chemical"]

def test_allocate_first_choice():
    assert student2 in allocatedStudents["chemical"]

def test_allocate_second_choice():
    assert student6 in allocatedStudents["software"]

def test_allocate_third_choice():
    assert student1 in allocatedStudents["civil"]

