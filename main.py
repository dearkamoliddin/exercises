

nums = [12, 34, 5, 3, 2, 423, 2, 23, 44]
"""Calculate sum of even numbers by using iterators"""
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
