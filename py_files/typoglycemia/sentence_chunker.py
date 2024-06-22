import re

# Example document string
document = 'Hello world. This is a test document. It contains several sentences.'

# Regular expression to split the text where a period is followed by a space or the end of the string
sentences = re.split(r'\.\s+|\.$', document)

# Print the list of sentences
print(sentences)