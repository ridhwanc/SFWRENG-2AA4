## @file testCalc.py
# @title testCalc
#  @Ridhwan Chowdhury , 400075426
#  @January 18th 2019


from ReadAllocationData import readStdnts, readFreeChoice, readDeptCapacity

from CalcModule import sort, average, allocate

import unittest

class TestCalc(unittest.TestCase):
    def setUp(self):
        self.expected = [{'macid': 'zadaina', 'gpa': [8.0]}, {'macid': 'chowdr11', 'gpa': [6.0]}, {'macid': 'khanr', 'gpa': [4.0]}]
    
    
    
    
    def test_sort(self):
        
        self.assertEqual(TypeError, TypeError)
        self.assertEqual(sort([{'macid': 'khanr', 'gpa': [4.0]}, {'macid': 'chowdr11', 'gpa': [6.0]}, {'macid': 'zadaina', 'gpa': [8.0]}]), self.expected)
    
    
    
    def test_average(self):
        exp_avg = 8.375
        self.assertEqual(average([{'macid': 'chowdr11', 'gender': 'male', 'gpa': [6.0]}, {'macid': 'zadaina', 'gender': 'male', 'gpa': [8.0]}, {'macid': 'khanr', 'gender': 'male', 'gpa': [4.0]}], 'male'), exp_avg)
        
        self.assertRaises(TypeError, average, [{'macid': 'chowdr11', 'gender': 'male', 'gpa': [6.0]}, {'macid': 'zadaina', 'gender': 'male', 'gpa': [8.0]}, {'macid': 'khanr', 'gender': 'male', 'gpa': 4.0}], 'male')
        
        self.assertRaises(UnboundLocalError, average, [{'macid': 'chowdr11', 'gender': 'male', 'gpa': [6.0]}, {'macid': 'zadaina', 'gender': 'male', 'gpa': [8.0]}, {'macid': 'khanr', 'gender': 'male', 'gpa': [4.0]}], 'female')
    
    
    
    
    def test_allocate(self):
        expected = {'engphys': [], 'civil': [], 'chemical': [], 'materials': [], 'electrical': [], 'mechanical': [], 'software': []}
        self.assertEqual(allocate(readStdnts("blank.txt"), readFreeChoice("blank.txt"), readDeptCapacity("departments.txt")), expected)
        
        expected2 = {'civil': [{'macid': 'zadaina', 'fname': 'Aws', 'lname': 'Zadain', 'gender': 'Male', 'gpa': 9.0, 'choices': ['civil', 'mechanical', 'software']}], 'chemical': [], 'electrical': [], 'mechanical': [], 'software': [{'macid': 'mostafn', 'fname': 'Mostafa', 'lname': 'Youngboy', 'gender': 'Male', 'gpa': 11.0, 'choices': ['software', 'mechanical', 'civil']}, {'macid': 'chowdr11', 'fname': 'Ridhwan', 'lname': 'Chowdhury', 'gender': 'Male', 'gpa': 6.0, 'choices': ['software', 'chemical', 'engphys']}], 'materials': [], 'engphys': []}
        self.assertEqual(allocate(readStdnts("readstudents.txt"), readFreeChoice("freechoice.txt"), readDeptCapacity("departments.txt")), expected2)



if __name__ == 'main':
    unittest.main()
