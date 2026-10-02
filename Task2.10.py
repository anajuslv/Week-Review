def letter_frequency():
    file = open("zen.txt", "r")

    text = file.read().lower()
    frequency = {}

    for letter in text:
        if letter.isalpha():
            if letter in frequency:
                frequency[letter] += 1
            else:
                frequency[letter] = 1

    for letter in sorted(frequency, key=frequency.get, reverse=True):
        print(letter, ":", frequency[letter])        

    file.close()


letter_frequency()