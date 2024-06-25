def analyze_sentence(sentence):
    # Remove punctuation and covert to lower case for uniformity.
    cleaned_sentence = ''.join(char.lower() if char.isalnum() or char.isspace() else '' for char in sentence)

    # Convert the cleaned sentence into a list of words
    words = cleaned_sentence.split()

    # Use set to find unique words, then sort them.

    unique_words = sorted(set(words))

    # Create a dictionary to count frequency of each word
    word_count = {word: words.count(word) for word in unique_words}

    return unique_words, word_count

# Prompt user to input a sentence

sentence = input("Please enter a sentence to analyze: ")

# Process the user input

unique_words, word_frequencies = analyze_sentence(sentence)

# Output
print(tuple(unique_words))
print(dict(word_frequencies))