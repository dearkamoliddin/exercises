

nums = [12, 34, 5, 3, 2, 423, 2, 23, 44]

num_iter = iter(nums)
summa = 0
while True:
    try:
        num = next(num_iter)
        if num % 2 == 0:
            summa += num
    except StopIteration:
        break

print("Sum of even numbers:", summa)



def fibonacci_numbers(nums):
    x, y = 0, 1
    for _ in range(nums):
        x, y = y, x+y
        yield x

def square(nums):
    for num in nums:
        yield num**2

print(sum(square(fibonacci_numbers(10))))