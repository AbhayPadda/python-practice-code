def factorial(n):
    factorial = 1
    if (n == 0):
        return factorial
    while (n > 0):
        factorial *= n
        n -= 1

    return factorial

def factorialUsingRecursion(n):
    if (n==1):
        return 1
    return n * factorialUsingRecursion(n - 1)

number = input ("Enter Number: ")
print (" Factorial of %d is : %d" %(int(number), factorial(int(number))))
print (" Factorial of %d using recursion is : %d" %(int(number), factorialUsingRecursion(int(number))))
       
