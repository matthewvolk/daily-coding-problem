# Given a 32-bit integer, return the number with its bits reversed.
# For example, given the binary number 1111 0000 1111 0000 1111 0000 1111 0000, 
# return 0000 1111 0000 1111 0000 1111 0000 1111.

import sys

class BitReversal:
  bit_sequence = ''
  reversed_bit_sequence = []

  def __init__(self, bit_sequence):
    self.bit_sequence = bit_sequence
  
  def reverse_bit_sequence(self):
    bit_sequence = list(self.bit_sequence)
    for bit in bit_sequence:
      if bit == '1':
        bit = '0'
        self.reversed_bit_sequence.append(bit)
      elif bit == '0':
        bit = '1'
        self.reversed_bit_sequence.append(bit)
      else:
        self.reversed_bit_sequence.append(bit) # if empty space, put back into bit sequence
    
    return ''.join(self.reversed_bit_sequence)


bit_sequence_to_reverse = BitReversal(sys.argv[1])
print(bit_sequence_to_reverse.reverse_bit_sequence())