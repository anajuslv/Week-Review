import unicodedata


def word_frequency():
    file = open("zen.txt", "r")

    words = file.read().split()
    frequency = {}

    for word in words:
        word = word.lower()
        word = word.strip(".,!?;:--*")

        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1

    for word in sorted(frequency):
        print(word, ":", frequency[word])

    file.close()


word_frequency()