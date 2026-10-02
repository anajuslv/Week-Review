ones = [
    "", "one", "two", "three", "four",
    "five", "six", "seven", "eight", "nine",
    "ten", "eleven", "twelve", "thirteen", "fourteen",
    "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"
]

tens = [
    "", "", "twenty", "thirty", "forty",
    "fifty", "sixty", "seventy", "eighty", "ninety"
]


def number_to_words(number):
    if number < 20:
        return ones[number]

    if number < 100:
        return tens[number // 10] + ones[number % 10]

    if number < 1000:
        result = ones[number // 100] + "hundred"

        if number % 100 != 0:
            result += "and" + number_to_words(number % 100)

        return result

    if number == 1000:
        return "onethousand"


def count_letters(N):
    total = 0

    for number in range(1, N + 1):
        words = number_to_words(number)
        total += len(words)

    return total


print(count_letters(5))
print(count_letters(42))
print(count_letters(1000))