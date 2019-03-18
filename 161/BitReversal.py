# Given a 32-bit integer, return the number with its bits reversed.
# For example, given the binary number 1111 0000 1111 0000 1111 0000 1111 0000, 
# return 0000 1111 0000 1111 0000 1111 0000 1111.

import sys

class BitManipulation:
  bit_sequence = ''

  def __init__(self, bit_sequence):
    self.bit_sequence = bit_sequence
  
  def flip_bits_in_sequence(self):
    flipped_bit_sequence = []
    bit_sequence = list(self.bit_sequence)
    for bit in bit_sequence:
      if bit == '1':
        bit = '0'
        flipped_bit_sequence.append(bit)
      elif bit == '0':
        bit = '1'
        flipped_bit_sequence.append(bit)
      else:
        flipped_bit_sequence.append(bit) # if empty space, put back into bit sequence
    return ''.join(flipped_bit_sequence)

  def reverse_bits_in_sequence(self):
    reversed_sequence = ''
    for bit in self.bit_sequence:
      reversed_sequence = bit + reversed_sequence
    return reversed_sequence


bit_sequence_to_reverse = BitManipulation(sys.argv[1])
print("\nBit Sequenced Flipped:")
print(bit_sequence_to_reverse.flip_bits_in_sequence() + "\n")

print("Bit Sequenced Reversed:")
print(bit_sequence_to_reverse.reverse_bits_in_sequence() + "\n")