'''
The four adjacent digits in the 1000-digit number 
that have the greatest product are 9 x 9 x 8 x 9 = 5832.
Find the thirteen adjacent digits in the 1000-digit number that
have the greatest product. What is the value of this product?
'''

def define_input_string():


  input_string = '''73167176531330624919225119674426574742355349194934 
96983520312774506326239578318016984801869478851843 
85861560789112949495459501737958331952853208805511
12540698747158523863050715693290963295227443043557
66896648950445244523161731856403098711121722383113
62229893423380308135336276614282806444486645238749
30358907296290491560440772390713810515859307960866
70172427121883998797908792274921901699720888093776
65727333001053367881220235421809751254540594752243
52584907711670556013604839586446706324415722155397
53697817977846174064955149290862569321978468622482
83972241375657056057490261407972968652414535100474
82166370484403199890008895243450658541227588666881
16427171479924442928230863465674813919123162824586
17866458359124566529476545682848912883142607690042
24219022671055626321111109370544217506941658960408
07198403850962455444362981230987879927244284909188
84580156166097919133875499200524063689912560717606
05886116467109405077541002256983155200055935729725
71636269561882670428252483600823257530420752963450'''

  return input_string

def process_input_string(input_string):
  input_string = "".join(input_string.split("\n"))
  input_string = "".join(input_string.split(" "))
  return input_string

def product_substring(s):
  if '0' in s:
    return 0
  total_product = 1
  for char in s:
    total_product *= int(char)

  return total_product

def get_largest_contiguous_product(input_array, k):
  '''
  Return the largest contiguous subarray product of size k
  Complexity can be O(n)
  '''

  max_product = 0
  
  for index in range(len(input_array)-k+1):
    current_product = product_substring(input_array[index:index+k])
    max_product = max(max_product,current_product)

  return max_product


def tests():
  input_array = "1233042312134221"
  assert get_largest_contiguous_product(input_array,2) == 12
  assert get_largest_contiguous_product(input_array,3) == 24
  assert get_largest_contiguous_product(input_array,4) == 48
  print("Tests successful")

if __name__ == "__main__":
  tests()
  input_array = define_input_string()
  input_array = process_input_string(input_array)  
  k = 13
  print(get_largest_contiguous_product(input_array,k))