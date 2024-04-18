
with open('test.txt', 'w') as file:
    """Write number from 1 to 100 to txt file"""
    for i in range(1, 101):
        file.write(str(i) + '\n')

