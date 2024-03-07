def count_negative_numbers(numbers):
    if not numbers:
        return 0
    count = 0
    if numbers[0] < 0:
        count += 1
    return count + count_negative_numbers(numbers[1:])


print(f"Количество отрицательных чисел: {count_negative_numbers([-2, 3, 8, -11, -4, 6])}")
