'''
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, 
we can see that the 6th prime is 13.

What is the 10 001st prime number?
'''


def is_prime(number,prime_list):
  '''
  Find out if a number is prime
  '''

  for prime in prime_list:
    if number % prime == 0:
      return False

  return True

def find_kth_prime(k):
  prime_list = [2]
  count = 1
  current_number = 3
  while count < k:
    if is_prime(current_number,prime_list):
      prime_list.append(current_number)
      count += 1
    current_number += 1

  return prime_list[k-1]


def test_is_prime():
  assert is_prime(11,[2,3,5,7]) == True
  assert is_prime(8,[2,3,5,7]) == False
  print("Is prime test successful")


def test_find_kth_prime():
  assert find_kth_prime(1) == 2
  assert find_kth_prime(5) == 11
  assert find_kth_prime(8) == 19
  print("Find kth prime test successful")


if __name__ == "__main__":
  test_is_prime()
  test_find_kth_prime()
  print(find_kth_prime(10001))