def prime(num):
    """Returns True if num is prime, False otherwise."""
    if num < 2:
     return False
    for i in range(2, num):
       if num % i == 0:
          return False
       return True
print(prime(7))