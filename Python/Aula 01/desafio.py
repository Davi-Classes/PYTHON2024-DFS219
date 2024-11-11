primes = []

start = int(input('Digite o numero de inicio: '))
final = int(input('Digite o numero final: '))

for number in range(start, final + 1):
    divisors_count = 0

    for n in range(1, number + 1):
        if number % n == 0:
            divisors_count += 1

    if divisors_count == 2:
        primes.append(number)

print(f'Numeros Primos: {primes}')