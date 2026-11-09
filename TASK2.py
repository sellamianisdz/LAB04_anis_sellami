
def addition(a, b):
    result = ""
    next = 0

    i = len(a) - 1
    j = len(b) - 1

    while i >= 0 or j >= 0 or next > 0:
        x = 0
        y = 0

        if i >= 0:
            x = int(a[i])

        if j >= 0:
            y = int(b[j])

        s = x + y + next

        result = str(s % 10) + result
        next = s // 10

        i = i - 1
        j = j - 1

    return result.lstrip("0") or "0"


def multiplication(a, b):
    result = [0] * (len(a) + len(b))

    i = len(a) - 1

    while i >= 0:
        j = len(b) - 1

        while j >= 0:
            x = int(a[i]) * int(b[j])
            x = x + result[i + j + 1]

            result[i + j + 1] = x % 10
            result[i + j] = result[i + j] + x // 10

            j = j - 1

        i = i - 1

    answer = ""

    for digit in result:
        answer = answer + str(digit)

    return answer.lstrip("0") or "0"


try:
    file = open("numbers.txt", "r")
    lines = file.readlines()
    file.close()

    if len(lines) != 2:
        print("The file must contain exactly two numbers.")

    else:
        a = lines[0].strip()
        b = lines[1].strip()

        if (not a.isdigit() or not b.isdigit()
                or len(a) > 200 or len(b) > 200):

            print("Invalid numbers. Use non-negative numbers with maximum 200 digits.")

        else:
            a = a.lstrip("0") or "0"
            b = b.lstrip("0") or "0"

            print("First number:", a)
            print("Second number:", b)
            print("Sum:", addition(a, b))
            print("Product:", multiplication(a, b))

except FileNotFoundError:
    print("The file numbers does not exist.")
