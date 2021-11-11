my_values = [2, 4, 5, 7, 9, 11, 14, 15, 17, 21, 24, 26, 28, 41, 48, 53, 68, 75, 98, 99]
primes = []
not_primes = []


for value in my_values:
    if value > 1:
        
        for i in range(2, value):

            if (value % i) == 0:
                primes.append(value)
                break
            else:
                not_primes.append(value)
                break

print("Prime Numbers:", primes)
print("Non-Prime Numbers:", not_primes)