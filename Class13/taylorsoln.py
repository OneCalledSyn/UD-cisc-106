def is_prime(n):
  primality = True
  for i in range(2,int(n**.5)+1):
    if (n % i == 0 or n == 1):
      primality = False
      break
  return primality

#print (is_prime(1))

numbers = range(2,51)

print(list(filter(is_prime, numbers)))