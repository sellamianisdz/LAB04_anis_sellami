
def is_prime(number):
    if number < 2:
      return False

    for i in range(2, number):
        if number % i == 0:
            return False

    return True


try:
    n = int(input("Enter an even number greater than 2: "))

    if n <= 2 or n % 2 != 0:
        print("Invalid number. Enter an even number greater than 2.")

    else:
        print("Goldbach decompositions:")

        for i in range(2, n // 2 + 1):
            j = n - i

            if is_prime(i) and is_prime(j):
                print(i, "+", j, "=", n)

except ValueError:
    print("Invalid input. Please enter a number.")
