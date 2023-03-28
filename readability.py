# Computes the approximate grade level needed to comprehend some text

# Modules
from cs50 import get_string

# Main program
def main():
	level = getGrade(getUserInput())

	if level <= 0:
		print("Before grade 1")
	elif level >= 16:
		print("Grade 16+")
	else:
		print(f"Grade {level}")

# Asks user for input
def getUserInput():
	userInput = get_string("Text: ")
	return userInput

# Computes grade using Coleman-Liau formula
def getGrade(text):
	letters = countLetters(text)
	words = countWords(text)
	sentences = countSentences(text)

	L = letters / words * 100
	S = sentences / words * 100
	index = 0.0588 * L - 0.296 * S - 15.8

	return round(index)

# Counts number of letters in a text
def countLetters(text):
	count = 0
	n = len(text)
	i = 0
	while i < n:
		if text[i].isalpha():
			count += 1
		i += 1

	return count

# Counts number of words in a text
def countWords(text):
	count = 1
	n = len(text)
	i = 0
	while i < n:
		if text[i] == " ":
			count += 1
		i += 1

	return count

# Counts number of sentences in a text
def countSentences(text):
	count = 0
	n = len(text)
	i = 0
	while i < n:
		if text[i] == "." or text[i] == "?" or text[i] == "!":
			count += 1
		i += 1

	return count


# Runs the program
main()
