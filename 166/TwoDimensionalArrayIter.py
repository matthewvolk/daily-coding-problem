# Implement a 2D iterator class. It will be initialized with an array of arrays, and should implement the following methods:

# next(): returns the next element in the array of arrays. If there are no more elements, raise an exception.
# has_next(): returns whether or not the iterator still has elements left.
# For example, given the input [[1, 2], [3], [], [4, 5, 6]], calling next() repeatedly should output 1, 2, 3, 4, 5, 6.

import sys

class TwoDimensionalArrayIter:
  twoDimensionalArr = []
  currentIndex1 = 0
  currentIndex2 = 0

  def __init__(self, arrOfArrs):
    self.twoDimensionalArr = arrOfArrs

  def getArrOfArrs(self):
    return self.twoDimensionalArr

  def next(self):
    for i in self.twoDimensionalArr:
      for j in i:
        # print("Inner Loop currentIndex2 = " + str(self.currentIndex2))
        # print("Inner Loop currentIndex1 = " + str(self.currentIndex1))
        # print("currentElement = " + str(j))
        self.currentIndex2 += 1
        # self.currentIndex1 = 0
      self.currentIndex1 += 1
      # print("Outer Loop currentIndex2 = " + str(self.currentIndex2))
      # print("Outer Loop currentIndex1 = " + str(self.currentIndex1))
    return self.currentIndex2

  def has_next(self):
    pass

arrOfArrsManipulator = TwoDimensionalArrayIter([[1, 1], [2, 2], [3, 3], [4, 4]])

# print(arrOfArrsManipulator.getArrOfArrs())
print(arrOfArrsManipulator.next())