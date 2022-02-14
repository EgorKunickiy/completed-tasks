
def sequence(n, m):
    for num in range(n, m+1):
        if num % 3 == 0:
            print('Fizz')
        elif num % 5 == 0:
            print('Buzz')
        elif num % 3 == 0 and num % 5 == 0:
            print('FizzBuzz')
        else:
            print(num)

if __name__ == '__main__':
    n = int(input())
    m = int(input())
    sequence(n, m)
