import random

numbers = [random.randint(1, 100) for _ in range(10)]
even = [n for n in numbers if n % 2 == 0]
odd = [n for n in numbers if n % 2 != 0]

print("Numbers:", numbers)
print("Even:", even)
print("Odd:", odd)

total = sum(numbers)
average = total / len(numbers)

print("Sum:", total)
print("Average:", round(average, 2))
print("Max:", max(numbers))
print("Min:", min(numbers))

squared = [n ** 2 for n in numbers]
print("Squared:", squared)

print("1")
