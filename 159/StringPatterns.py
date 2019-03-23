# Given a string, return the first recurring character in it, or null if there is no recurring character.
# For example, given the string "acbbac", return "b". Given the string "abcdef", return null.

import sys

class StringPatterns:
  st = ''

  def __init__(self, st):
    self.st = st

  def first_recurring_char(self):
    prev_chars = []

    for i in self.st:
      print("========================================================")
      print(prev_chars)
      # prev_chars.append(i)
      print("outer loop i = " + i)
      for j in prev_chars:
        # print("i = " + i)
        # print("j = " + j)
        # prev_chars.append(i)
        if i == j:
          print("inner loop i = " + i + "\ninner loop j = " + j + "\n" + "repeating char detected! \n")
          break
        else:
          print("inner loop i = " + i + "\ninner loop j = " + j + "\n" + "no repeaters \n")
          break
    # return i

      # id first recurring char in string
      # return char if it is recurring
      # return null if no recurring string

string_sequence = StringPatterns(sys.argv[1])
print(string_sequence.first_recurring_char())