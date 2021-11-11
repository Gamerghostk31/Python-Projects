#List to check
numbers = [2, 3, 5, 7, 9, 11, 13, 17, 19, 20, 23, 29, 30, 31, 36, 37, 41, 43, 45, 47, 53, 59,
 61, 64, 67, 69, 71, 73, 79, 83, 89, 97, 101, 105, 115, 140, 270, 420, 69420]

#Empty Lists
only_primes = []
non_primes = []

for x in numbers:
    if x == 2:
        only_primes.append(x)
    else:
        for n in range(2, x):
            if n % x == 0:
                non_primes.append(x)
            else:
                only_primes.append(x)

print("List of primes:\n" + str(only_primes))
print("")
print("List of non-primes:\n" + str(non_primes))
      