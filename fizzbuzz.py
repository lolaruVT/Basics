for x in range(1, 21):
    if x % 3 == 0 and x & 5 == 0:
        print('FizzBuzz')
        continue
    if x % 3 == 0:
        print('Fizz')
        continue
    if x % 5 == 0:
        print('Buzz')
        continue
    print(x)
    