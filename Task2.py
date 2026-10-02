#Task 2.8
def longest():
    file = open("zen.txt", "r")

    words = file.read().split()

    longest_word = max(words, key=len)

    print(longest_word)

    file.close()


longest()


