class TextProcessor:
    def __init__(self, text):
        """
        Initialize the TextProcessor with a specific text.

        Args:
            text (str): The text to be processed.
        """
        self.text = text

    def capitalize_text(self):
        """
        Capitalizes the first letter of each word in the text.
        Useful for formatting titles or emphasizing each word.

        Returns:
            str: The text with each word capitalized.
        """
        return ' '.join(word.capitalize() for word in self.text.split())

    def count_words(self):
        """
        Counts the number of words in the text.
        This method can be used to get an idea of text length in terms of words.

        Returns:
            int: The number of words in the text.
        """
        return len(self.text.split())

    def find_word(self, word):
        """
        Checks if a specific word exists in the text, insensitive to case.
        
        Args:
            word (str): The word to search for in the text.

        Returns:
            bool: True if the word is found, False otherwise.
        """
        return word.lower() in self.text.lower().split()

    def reverse_text(self):
        """
        Reverses the given text.
        This can be used for creating palindromes or for encryption simulations.

        Returns:
            str: The reversed version of the text.
        """
        return self.text[::-1]

    def get_word_frequency(self):
        """
        Returns a dictionary with the frequency of each word in the text.
        This method can be useful for text analysis, such as identifying the most common words.

        Returns:
            dict: A dictionary where the keys are words and the values are their frequencies.
        """
        words = self.text.lower().split()
        frequency = {}
        for word in words:
            if word in frequency:
                frequency[word] += 1
            else:
                frequency[word] = 1
        return frequency

# Example usage:
text = "hello world world"
processor = TextProcessor(text)

print("Capitalized Text:", processor.capitalize_text())
print("Word Count:", processor.count_words())
print("Word 'world' Found:", processor.find_word("world"))
print("Reversed Text:", processor.reverse_text())
print("Word Frequency:", processor.get_word_frequency())
