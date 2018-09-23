"""
A permutation is an ordered arrangement of objects. 
For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. 
If all of the permutations are listed numerically or alphabetically, 
we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
"""
import math

def binary_search(n,p):
  """
  Computes the index in which the result lies
  Args:
    n: number of permutations
    p: number of digits

  Returns:
    search index

  """
  start = 0
  end = p-1
  while end > start + 1:
    mid = math.ceil((start + end)/2)
    if mid*math.factorial(p-1) < n:
      start = mid
    else:
      end = mid

  if start == end:
    return start
    
  if end == start + 1:
    if end*math.factorial(p-1) < n:
      return end
    else:
      return start



def lexicographic_permutation(n,digits):
  """
  Find the nth lexicographic permutation 
  given a set of digits

  Solve through recursive binary search
  """

  # Base case
  if len(digits) == 1:
    return str(digits[0])

  sorted_digits = sorted(digits)
  search_index = int(binary_search(n,len(digits)))
  search_digit = sorted_digits[search_index]
  sorted_digits.remove(sorted_digits[search_index])
  count = search_index*math.factorial((len(digits) - 1))
  return str(search_digit) + \
      lexicographic_permutation(n - count, \
                sorted_digits)

def test_binary_search():
  assert binary_search(5,3) == 2
  assert binary_search(2,3) == 0
  assert binary_search(3,3) == 1
  assert binary_search(1,3) == 0
  assert binary_search(25,5) == 1
  assert binary_search(67,5) == 2

def test():
  assert lexicographic_permutation(5,[0,1,2]) == "201"
  assert lexicographic_permutation(9,[0,1,2,3]) == "1203"


if __name__ == "__main__":
  test_binary_search()
  test()
  print(lexicographic_permutation(1e+6,range(10)))