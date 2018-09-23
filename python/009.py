'''
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
'''


def find_pythagorean_triplet_respecting_sum(triplet_sum=1000):
  for a in range(1,triplet_sum):
    for b in range(a+1,triplet_sum-a):
      c = triplet_sum - a - b
      if a**2 + b**2 == c**2:
        return (a,b,c)


def product_pythagorean_triplet(triplet_sum=1000):
  (a,b,c) = find_pythagorean_triplet_respecting_sum(triplet_sum)
  return a*b*c


def tests():
  assert product_pythagorean_triplet(12) == 60
  assert product_pythagorean_triplet(30) == 780

  print("Tests successful")

if __name__ == "__main__":
  tests()
  print(product_pythagorean_triplet(1000))
