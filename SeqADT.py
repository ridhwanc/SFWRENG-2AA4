## @file SeqADT.py
# @title SequenceADT Module
# @author Ridhwan Chowdhury
# @date February12


## @brief A sequence abstract data type
class SeqADT():
    ## @brief Initializes the sequence
    # @param x parameter represents the sequence
    def __init__(self, x):
        self.s = x
        self.i = 0

    ## @brief Commences the sequence
    def start(self):
        self.i = 0

    ## @brief Moves to the next element in the sequence and returns that part of the sequence
    # @details If the element reaches the end of the sequence, stop the iteration
    # @return returns choice: the department indexed by the element
    def next(self):
        if self.i >= len(self.s):
            raise StopIteration
        else:
            choice = self.s[self.i]
            self.i = self.i + 1
            return choice

    ## @brief Moves to the next element in the sequence
    # @details If the element reaches the end of the sequence, return True, if
    # elements still remain, return false
    # @return returns choice: the department indexed by the element
    def end(self):
        if self.i >= len(self.s):
            return True
        else:
            return False
