"""
Exercise-1: is_prime
Write a function "is_prime(n: int) -> bool" that takes an integer 'n' 
and checks whether it is prime. Function should return a boolean value.

Example:
is_prime(7) -> True
is_prime(10) -> False
"""

def is_prime(n: int) -> bool:
    if n == 2:
        return True
    elif n<2: return False
    for i in range(2, n):
        if n > 1 and n % i > 0:
            return True
        else:
            return False

    # write your code here
    pass

"""
Exercise-2: nth_fibonacci
Write a function "nth_fibonacci(n: int) -> int" that 
takes an integer 'n' and returns the nth number in the Fibonacci sequence.

Example:
nth_fibonacci(6) -> 5
nth_fibonacci(9) -> 21
"""

def nth_fibonacci(n: int) -> int:
    # write your code here
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else: return nth_fibonacci(n-1) + nth_fibonacci(n-2)

    pass

"""
Exercise-3: factorial
Write a function "factorial(n: int) -> int" that takes an integer 'n' and returns the factorial of 'n'.

Example:
factorial(5) -> 120
factorial(6) -> 720
"""

def factorial(n: int) -> int:
    # write your code here
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else: return n * factorial(n-1)

    pass

"""
Exercise-4: count_vowels
Write a function "count_vowels(s: str) -> int" that 
takes a string 's' and returns the number of vowels in the string.

Example:
count_vowels("hello") -> 2
count_vowels("world") -> 1
"""

def count_vowels(s: str) -> int:
    # write your code here
    count = 0
    for i in s:
        if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u' or i == 'A' or i == 'E' or i == 'I' or i == 'O' or i == 'U':
            count += 1

    return count
    pass

"""
Exercise-5: sum_of_digits
Write a function "sum_of_digits(n: int) -> int" that 
takes an integer 'n' and returns the sum of its digits.

Example:
sum_of_digits(12345) -> 15
sum_of_digits(98765) -> 35
"""

def sum_of_digits(n: int) -> int:
    # write your code here
    sum = 0
    numbers = str(abs(n))
    for i in numbers:
        sum+=int(i)

    return sum

    pass


"""
Exercise-6: reverse_string
Write a function "reverse_string(s: str) -> str" that takes a string 's' and returns the string reversed.

Example:
reverse_string("hello") -> "olleh"
reverse_string("world") -> "dlrow"
"""

def reverse_string(s: str) -> str:
    # write your code here
    return s[::-1]
    pass


"""
Exercise-7: sum_of_squares
Write a function "sum_of_squares(n: int) -> int" that takes an integer 'n' and 
returns the sum of squares of all integers from 1 to 'n'.

Example:
sum_of_squares(4) -> 30
sum_of_squares(5) -> 55
"""

def sum_of_squares(n: int) -> int:
    # write your code here
    sum_sq = 0
    i = 1
    while i <= n:
        sum_sq += i*i
        i += 1

    return sum_sq
    pass


"""
Exercise-8: collatz_sequence_length
Write a function "collatz_sequence_length(n: int) -> int" that takes an 
integer 'n' and returns the length of the Collatz sequence starting with 'n'.

Example:
collatz_sequence_length(6) -> 9
collatz_sequence_length(27) -> 112
"""

def collatz_sequence_length(n: int) -> int:
    # write your code here
    count = 1
    while n != 1:
        if n % 2 == 0:
            n = n // 2
            count += 1
        elif n % 2 == 1:
            n = 3 * n + 1
            count += 1

    return count
    pass


"""
Exercise-9: is_leap_year
Write a function "is_leap_year(year: int) -> bool" that takes an 
integer 'year' and returns True if 'year' is a leap year, and False otherwise.

Example:
is_leap_year(2000) -> True
is_leap_year(1900) -> False
"""

def is_leap_year(year: int) -> bool:
    # write your code here
    if year % 400 == 0 and year % 100 == 0:
        return True
    elif year % 4 == 0 and year % 100 != 0:
        return True
    else:
        return False
    pass


"""
Exercise-10: count_words
Write a function "count_words(s: str) -> int" that takes a string 's' and 
returns the number of words in the string. Assume words are separated by spaces.

Example:
count_words("Hello world") -> 2
count_words("This is a test") -> 4
"""

def count_words(s: str) -> int:
    # write your code here
    count = 0

    if s == "":
        return 0
    else:
        for i in s.split(" "):
            if i == "":
                pass
            else:
                count += 1
    return count
    pass


"""
Exercise-11: is_palindrome
Write a function "is_palindrome(s: str) -> bool" that takes a string 's' and 
checks if the string is a palindrome. The function should return True if the 
string is a palindrome, and False otherwise.

Example:
is_palindrome("racecar") -> True
is_palindrome("hello") -> False
"""

def is_palindrome(s: str) -> bool:
    # write your code here
    if s == "":
        return True
    else:
        for i in range(0, len(s)):
            if s[i] == s[-(i + 1)]:
                return True
            else:
                return False
    pass

"""
Exercise-12: sum_of_multiples
Write a function "sum_of_multiples(n: int, x: int, y: int) -> int" that 
takes three integers 'n', 'x', and 'y', and returns the sum of all the 
numbers from 1 to 'n' (inclusive) that are multiples of 'x' or 'y'.

Example:
sum_of_multiples(10, 3, 5) -> 33
sum_of_multiples(20, 7, 11) -> 168
"""

def sum_of_multiples(n: int, x: int, y: int) -> int:
    # write your code here
    sum = 0
    for i in range(0, n + 1):
        if i % x == 0 or i % y == 0:
            sum += i

    return sum
    pass


"""
Exercise-13: gcd
Write a function "gcd(a: int, b: int) -> int" that takes two integers 'a' and 'b', 
and returns their greatest common divisor (GCD).

Example:
gcd(56, 98) -> 14
gcd(27, 15) -> 3
"""

def gcd(a: int, b: int) -> int:
    # write your code here
    if a == 0 or b == 0:
        return 0

    biggest_gcd = 1
    for i in range(2, a):
        if a % i == 0 and b % i == 0:
            biggest_gcd = i
    return biggest_gcd
    pass


"""
Exercise-14: lcm
Write a function "lcm(a: int, b: int) -> int" that takes two integers 'a' and 'b', 
and returns their least common multiple (LCM).

Example:
lcm(5, 7) -> 35
lcm(6, 8) -> 24
"""

def lcm(a: int, b: int) -> int:
    # write your code here
    highest_lcm = a * b
    if a == 0 or b == 0:
        return 0
    for i in range(1, highest_lcm + 1):
        if i % a == 0 and i % b == 0:
            return i
    pass


"""
Exercise-15: count_characters
Write a function "count_characters(s: str, c: str) -> int" that 
takes a string 's' and a character 'c', and returns the number of occurrences of 'c' in 's'.

Example:
count_characters("hello world", "l") -> 3
count_characters("apple", "p") -> 2


"""

def count_characters(s: str, c: str) -> int:
    # write your code here
    count = 0
    for i in s:
        if i == c:
            count += 1

    return count
    pass


"""
Exercise-16: digit_count
Write a function "digit_count(n: int) -> int" that takes an 
integer 'n' and returns the number of digits in 'n'.

Example:
digit_count(123) -> 3
digit_count(4567) -> 4
"""

def digit_count(n: int) -> int:
    # write your code here
    count = 0
    for i in str(n):
        count += 1

    return count
    pass


"""
Exercise-17: is_power_of_two
Write a function "is_power_of_two(n: int) -> bool" that takes an integer 'n' 
and returns True if 'n' is a power of 2, and False otherwise.

Example:
is_power_of_two(8) -> True
is_power_of_two(10) -> False
"""

def is_power_of_two(n: int) -> bool:
    # write your code here
    if n <= 0:
        return False
    while n % 2 == 0:
        n = n // 2
    return n == 1
    pass


"""
Exercise-18: sum_of_cubes
Write a function "sum_of_cubes(n: int) -> int" that takes an integer 'n' 
and returns the sum of the cubes of all numbers from 1 to 'n'.

Example:
sum_of_cubes(3) -> 36
sum_of_cubes(4) -> 100
"""

def sum_of_cubes(n: int) -> int:
    # write your code here
    i = 1
    sum_of_cubes = 0
    while i <=n:
        sum_of_cubes += i ** 3
        i+=1
    return sum_of_cubes
    pass


"""
Exercise-19: is_perfect_square
Write a function "is_perfect_square(n: int) -> bool" that takes an 
integer 'n' and returns True if 'n' is a perfect square, and False otherwise.

Example:
is_perfect_square(9) -> True
is_perfect_square(10) -> False
"""

def is_perfect_square(n: int) -> bool:
    # write your code here
    a = n ** .5
    if n >= 0 and a == int(a):
        return True
    else:
        return False
    pass


"""
Exercise-20: is_armstrong_number
Write a function "is_armstrong_number(n: int) -> bool" that takes an 
integer 'n' and returns True if 'n' is an Armstrong number, and False otherwise.

Example:
is_armstrong_number(153) -> True
is_armstrong_number(370) -> True
"""

def is_armstrong_number(n: int) -> bool:
    # write your code here
    count = 0
    num_of_digits = str(n)
    for i in num_of_digits:
        count += int(i) ** len(num_of_digits)

    return count == n
    pass