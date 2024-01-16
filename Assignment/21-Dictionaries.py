def count_word_and_letter(text):
    word_count = {}
    letter_count = {}
    for word in text.split():
        word_count[word] = word_count.get(word, 0) + 1
        for letter in word:
            if letter.isalpha():
                letter_count[letter] = letter_count.get(letter, 0) + 1
    return word_count, letter_count

def invert_dictionary(dictionary):
    inverted_dictionary = {value: key for key, value in dictionary.items()}
    return inverted_dictionary

long_text = "This is a long text with some repeated words and letters."

word_occurrences, letter_occurrences = count_word_and_letter(long_text)

print("Word Occurrences:", word_occurrences)
print("Letter Occurrences:", letter_occurrences)

inverted_word_occurrences = invert_dictionary(word_occurrences)
inverted_letter_occurrences = invert_dictionary(letter_occurrences)

print("Inverted Word Occurrences:", inverted_word_occurrences)
print("Inverted Letter Occurrences:", inverted_letter_occurrences)
