def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list
    if all(num == 0 for num in numbers):
        return 0  # Handle list with only zeros
    total = sum(numbers)
    return total / len(numbers)