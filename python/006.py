'''
The sum of the squares of the first ten natural numbers is,

12 + 22 + ... + 102 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)2 = 552 = 3025
Hence the difference between the sum of the squares of the 
first ten natural numbers and the square of the sum is 3025 - 385 = 2640.

Find the difference between the sum of the squares of the first 
one hundred natural numbers and the square of the sum.
'''


def sum_of_squares_diff_square_of_sum(n):
  return (n*(n+1)/2)**2 - (n*(n+1)*(2*n + 1)/6)


def tests():
  assert sum_of_squares_diff_square_of_sum(2) == 4
  assert sum_of_squares_diff_square_of_sum(10) == 2640
  print("Tests successful")

if __name__ == "__main__":
  tests()

  # Difference for first 100 natural numbers
  print(sum_of_squares_diff_square_of_sum(100))