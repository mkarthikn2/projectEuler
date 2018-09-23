"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

import math
import time

def is_prime(n):

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

def sum_primes(limit):
  current_sum = 5
  n = 5
  while n <= limit:
    if is_prime(n):
      current_sum += n
    n = n + 2
    if n <= limit and is_prime(n):
      current_sum += n
    n += 4

  return current_sum

def test_is_prime():
  assert is_prime(5) == True
  assert is_prime(7) == True
  assert is_prime(37) == True
  assert is_prime(91) == False
  assert is_prime(101) == True


def test_sum_primes():
  assert sum_primes(4) == 5
  assert sum_primes(6) == 10
  assert sum_primes(7) == 17
  assert sum_primes(12) == 28

if __name__ == "__main__":
  test_is_prime()
  test_sum_primes()
  t1 = time.time()
  z = sum_primes(2000000)
  print(time.time() - t1)
  print("Sum = ", z)