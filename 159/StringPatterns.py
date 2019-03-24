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
      if (i in prev_chars) == True:
        return i
      prev_chars.append(i)
    
    return None

string_sequence = StringPatterns(sys.argv[1])
print(string_sequence.first_recurring_char())