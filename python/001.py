'''
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
'''

import math


def solution(N,multiples_list):
  all_permissable_numbers = []
  for multiple in multiples_list:
    max_scale = N/multiple - 1 if N%multiple == 0 else int(N/multiple)
    all_permissable_numbers += [multiple*k for k in range(max_scale+1)]
  return sum(set(all_permissable_numbers))



if __name__ == "__main__":
  N = 10
  multiples_list = [3,5]
  print(solution(N,multiples_list))