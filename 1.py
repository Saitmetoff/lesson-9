"""1"""

import threading

def func1():
    print("Function 1 is running")

def func2():
    print("Function 2 is running")

def func3():
    print("Function 3 is running")

def func4():
    print("Function 4 is running")

t1 = threading.Thread(target=func1)
t2 = threading.Thread(target=func2)
t3 = threading.Thread(target=func3)
t4 = threading.Thread(target=func4)

t1.start()
t2.start()
t3.start()
t4.start()

t1.join()
t2.join()
t3.join()
t4.join()



"""2"""

from multiprocessing import Process

def sum_of_numbers(numbers):
    total = sum(numbers)
    print(f"Sum of numbers: {total}")

if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5]
    process = Process(target=sum_of_numbers, args=(numbers,))
    process.start()
    process.join()


"""3"""

def print_names_with_a(filename):
    with open(filename, "r") as file:
        names = file.readlines()
        for name in names:
            if name.strip().lower().startswith("a"):
                print(name.strip())

if __name__ == "__main__":
    filename = "input.txt"
    print_names_with_a(filename)


"""4"""

def print_long_names(filename):
    with open(filename, "r") as file:
        names = file.readlines()
        for name in names:
            if len(name.strip()) > 5:
                print(name.strip())

if __name__ == "__main__":
    filename = "input.txt"
    print_long_names(filename)


"""5"""

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def check_numbers(numbers):
    for num in numbers:
        if is_prime(num):
            print(f"{num} tub son")
        else:
            print(f"{num} murakkab son")

if __name__ == "__main__":
    numbers = [6, 31415926535897932384626433832795, 1, 3, 10, 3, 5]
    check_numbers(numbers)


"""6"""

def sort_non_negative_integers(numbers):
    non_negative_numbers = [num for num in numbers if num >= 0]
    sorted_numbers = sorted(non_negative_numbers)
    for num in sorted_numbers:
        print(num)

if __name__ == "__main__":
    N = 12
    numbers = [6, 31415926535897932384626433832795, 1, 3, 10, 3, 5]
    sort_non_negative_integers(numbers)


"""7"""

def remove_duplicate_chars(s):
    unique_chars = []
    for char in s:
        if char not in unique_chars:
            unique_chars.append(char)
    return "".join(unique_chars)

if __name__ == "__main__":
    S = "aaabccddd"  # Sizga berilgan S satri
    result = remove_duplicate_chars(S)
    print(result)


"""8"""

def megamix_comparison(numbers):
    def beauty_score(num):
        return sum(int(digit) for digit in str(num))

    max_beauty_score = 0
    max_beauty_number = None

    for num in numbers:
        score = beauty_score(num)
        if score > max_beauty_score:
            max_beauty_score = score
            max_beauty_number = num

    print(max_beauty_number)

if __name__ == "__main__":
    numbers = [6, 31415926535897932384626433832795, 1, 3, 10, 3, 5]
    megamix_comparison(numbers)
