def is_prime(n):
  primality = True
  for i in range(2,int(n**.5)):
    if n % i == 0:
      primality = False
      break
  return primality

print(is_prime(9))