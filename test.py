print("Write number from 1 to 100 to txt file")
with open('test.txt', 'w') as file:
    for i in range(1, 101):
        file.write(str(i) + '\n')

