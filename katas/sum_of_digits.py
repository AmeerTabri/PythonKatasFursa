def sum_of_digits(input_str):
    # return sum(int(char) for char in input_str if char.isdigit())
    digits_sum = 0
    for char in input_str:
        if 0 <= ord(char) - ord('0') <= 9:
            digits_sum += int(char)
    return digits_sum

if __name__ == '__main__':
    input1 = "abc123"
    input2 = "5 cats and 2 dogs"
    input3 = "No digits here!"

    print(f"Sum of digits in '{input1}': {sum_of_digits(input1)}")  # Should be 6
    print(f"Sum of digits in '{input2}': {sum_of_digits(input2)}")  # Should be 7
    print(f"Sum of digits in '{input3}': {sum_of_digits(input3)}")  # Should be 0
