'''
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''
import time

def find_largest_prime_factor(n,k):
  '''
  Find the largest prime factor greater or equal to k
  '''


  while n > k:
    while n%k == 0:
      n = n/k

    k = k + 1

  return n


def tests():

  assert find_largest_prime_factor(10,2) == 5
  assert find_largest_prime_factor(13,2) == 13
  assert find_largest_prime_factor(39,2) == 13
  print("Tests successful")
  


def main():
  k = 2
  n = 600851475143
  tests()
  t1 = time.time()
  print(find_largest_prime_factor(n,2))
  print(time.time() - t1)


if __name__ == "__main__":
  main()