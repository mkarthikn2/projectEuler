"""
It was proposed by Christian Goldbach that every odd composite number 
can be written as the sum of a prime and twice a square.
9 = 7 + 2x12
15 = 7 + 2x22
21 = 3 + 2x32
25 = 7 + 2x32
27 = 19 + 2x22
33 = 31 + 2x12

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?

"""
import math

def is_prime(n):

  if n == 1:
    return False

  if n == 2:
    return True

  if n == 3:
    return True

  # Multiple of 2
  if n % 2 == 0:
    return False

  # Multiple of 3
  elif n % 3 == 0:
    return False

  else:
    r = math.floor(math.sqrt(n))
    f = 5
    while f <= r:
      if n % f == 0:
        return False
      elif n  % (f + 2) == 0:
        return False
      f = f + 6

    return True



def first_k_violations_goldbach(k):
  """
  Return the first k violations of the 
  Goldbach conjecture
  """

  violations = []
  n = 9
  while len(violations) < k:
    if n % 2 == 0:
      n = n + 1
      continue

    if is_prime(n):
      n = n + 1
      continue

    num = 1
    while n - 2*num**2 >= 2:
      if is_prime(n - 2*num**2):
        n = n + 1
        break
      num += 1

    if n - 2*num**2 < 2:
      violations.append(n)
      n = n  + 1

  return violations



if __name__ == "__main__":
  print(first_k_violations_goldbach(1))





