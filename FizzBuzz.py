
def sequence(n: int, m: int):
    for num in range(n, m+1):
        if num % 3 == 0 and num % 5 == 0:
            print('FizzBuzz')
        elif num % 3 == 0:
            print('Fizz')
        elif num % 5 == 0:
            print('Buzz')
        else:
            print(num)

if __name__ == '__main__':
    n = int(input())
    m = int(input())
    sequence(n, m)
