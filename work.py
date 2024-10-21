def is_armstrong_number(n: int) -> bool:
    # write your code here
    count = 0
    num_of_digits = str(n)
    for i in num_of_digits:
        count += int(i) ** len(num_of_digits)

    return count == n

    pass

print(is_armstrong_number(370))