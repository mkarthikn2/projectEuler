'''
A palindromic number reads the same both ways. 
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99.
Find the largest palindrome made from the product of two 3-digit numbers.
'''


def is_divisible_by_three_digit(number):
  '''
  Return true if it is divisible 
  by 3 digit number. Else return False
  '''

  for ind in range(100,999):
    if number % ind == 0 and number/ind < 1000:
      print (ind,number/ind)
      return True

  return False



def largest_palindrome_from_product_of_3digit_numbers():
  for first_digit in range(9,0,-1):
    for second_digit in range(9,-1,-1):
      for third_digit in range(9,-1,-1):
        number = first_digit*1e+5 + second_digit*1e+4 + \
                  third_digit*1e+3 + third_digit*1e+2 + \
                  second_digit*1e+1 + first_digit*1e+0
        if is_divisible_by_three_digit(number):
          return number


if __name__ == "__main__":
  print(largest_palindrome_from_product_of_3digit_numbers())

