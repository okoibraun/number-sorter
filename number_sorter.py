#!/usr/bin/python
import os
import argparse

# Bubble sorting algorithm
def sort_bubble(numbers):
  for sorted in reversed(range(len(numbers[1:]))):
      for index in range(len(numbers[:sorted])):
          if numbers[index] > numbers[index + 1]:
            numbers[index], numbers[index + 1] = numbers[index + 1], numbers[index]
  return numbers

# Insertion sorting algorithm
def sort_insertion(numbers):
  for index in range(1, len(numbers)):
    for i in reversed(range(index)):
      if numbers[index] < numbers[i]:
        numbers[index], numbers[i] = numbers[i], numbers[index]
  return numbers

# Selection sorting algorithm
def sort_selection(numbers):
  for index in range(len(numbers)):
        index_min = index + numbers[index:].index(min(numbers[index:]))
        numbers[index], numbers[index_min] = numbers[index_min], numbers[index]
  return numbers

# Argument parser
parser = argparse.ArgumentParser()
parser = argparse.ArgumentParser(description='Sort a file containing numbers')
parser.add_argument('file_in',  
                    type=str,  
                    help='file containing unsorted numbers')
parser.add_argument('file_out', 
                    type=str, 
                    nargs='?',
                    default='sorted_numbers.txt', 
                    help='file to write sorted number to')
parser.add_argument('-d','--delimiter',
                    type=str,
                    default='\n', 
                    help='specify what delimiter to use')
parser.add_argument('-o','--order',
                    choices=['ascending','descending'],
                    default='ascending',
                    help='specify how numbers should be ordered')
parser.add_argument('-s','--sorting-algorithm',
                    choices=['bubble','insertion','selection'],
                    default='selection',
                    help='specify what sorting algorithm to use')
args = parser.parse_args()


# Read file
numbers = list(map(int, open(args.file_in,'r').read().split(args.delimiter)))

# Sort numbers
{
    'bubble' : sort_bubble(numbers),
    'insertion' : sort_insertion(numbers),
    'selection' : sort_selection(numbers)
}[str(args.sorting_algorithm)]

# Order ascending or descending
if str(args.order) == 'descending' : numbers = reversed(numbers) 

# Write file
open(args.file_out, 'w').write(args.delimiter.join(map(str, numbers)))