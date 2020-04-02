def simpleGenerator(numbers):
    i = 0
    while True:
        check = input('Wanna generate a number? (If yes, press y else n): ')
        if check in ('Y', 'y') and len(numbers) > i:
            yield numbers[i]
            i += 1
        else:
            print('Bye!')
            break

for number in simpleGenerator([10, 11, 12, 14]):
    print(number)