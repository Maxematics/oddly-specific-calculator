# Returns sqrt(n) rounded to a number of decimals
def sqrt(n, precision):
    if n < 0:
        return "Error: Negative Square Root"
    if precision < 0:
        return "Error: Precision Can't Be Negative"
    if precision % 1 != 0.0:
        return "Error: Precision Can't Be Decimal"
    if precision > 10:
        return "Error: Too Long Decimal"
    precision = int(precision)
    p1 = 0
    p2 = n
    r = pow(10, -precision - 1)
    while p1 < p2:
        m = round((p1 + p2) / 2, precision + 1)
        if m * m < n:
            p1 = m + r
        else:
            p2 = m - r
    return round(p1, precision)

# Euclidean Algorithm
def gcd(a, b):
    if a % 1 != 0.0 or b % 1 != 0.0:
        return "Error: Input Must Be Integer"
    a, b = int(a), int(b)
    while b != 0:
        a, b = b, a % b
    return abs(a)

# Factorizes n into prime factors
def factor(n):
    if n % 1 != 0.0:
        return "Error: Input Must Be Integer"
    n = int(n)

    # Warning for time
    if n > pow(10, 16):
        print(f"Note: this may take up to {sqrt(n, 0) / 100000000} second(s). Type \"yes\" to contine")
        r = input()
        if r.lower() != "yes":
            return "Calculation cancelled."
        
    r = []
    while n % 2 == 0:
        n >>= 1
        r.append(2)
    for i in range(3, int(sqrt(n, 0)), 2):
        while n % i == 0:
            n //= i
            r.append(i)
    if n != 1:
        r.append(n)
    return " ".join(map(str, r))

# Returns n! (n factorial)
def factorial(n):
    if n % 1 != 0.0:
        return "Error: Input Must Be Integer"
    n = int(n)
    if n < 0:
        return "Error: Input Must Be Positive"
    if n > 100:
        return "Error: Too Large Result"
    t = 1
    for i in range(2, n + 1):
        t *= i
    return t

# Repeated loop
while True:
    s = input().split()

    if s[0].lower() == "sqrt":
        if len(s) == 2:
            try:
                print(sqrt(float(s[1]), 0))
            except:
                print("Error: Invalid Number")
        elif len(s) == 3:
            try:
                print(sqrt(float(s[1]), float(s[2])))
            except:
                print("Error: Invalid Number")
        else:
            print("Error: Incorrect Formatting")
            

    elif s[0].lower() == "gcd":
        if len(s) == 3:
            try:
                print(gcd(float(s[1]), float(s[2])))
            except:
                print("Error: Invalid Number")
        else:
            print("Error: Incorrect Formatting")


    elif s[0].lower() == "factor":
        if len(s) == 2:
            try:
                print(factor(float(s[1])))
            except:
                print("Error: Invalid Number")
        else:
            print("Error: Incorrect Formatting")
    
    elif s[0].lower() == "factorial":
        if len(s) == 2:
            try:
                print(factorial(float(s[1])))
            except:
                print("Error: Invalid Number")
        else:
            print("Error: Incorrect Formatting")

    elif s[1].lower() == "factorial":
        if len(s) == 2:
            try:
                print(factorial(float(s[0])))
            except:
                print("Error: Invalid Number")
        else:
            print("Error: Incorrect Formatting")
    
    elif s[0].lower() == "exit":
        print("Thank you!")
        break

    else:
        print("Error: Keyphrase not found")
    print("\n")