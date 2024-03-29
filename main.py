def main():
	book_path = "books/frankenstein.txt"
	book_text = get_book_text(book_path)

	frankenstein_words = word_count(book_text)
	frankenstein_letters = letter_count(book_text)
	print_report(book_path, frankenstein_words, frankenstein_letters)


# Getting Text
def get_book_text(path):
	with open(path) as f:
		return f.read()


# Counting Words
def word_count(text):
	count = 0
	words = text.split()

	for word in words:
		count += 1
	return count


# Counting Letters
def letter_count(text):
	count = {}
	words = text.lower().split()
	
	for word in words:
		for letter in word:
			if letter not in count and letter.isalpha() :
				count[letter] = 1
			elif letter.isalpha() :
				count[letter] += 1
			else:
				pass
	return count


def print_report(path, word_count, letter_count):
	# words -> int
	# letters -> {letter: int}
	
	print(f"--- Begin report of {path} ---")
	print(f"{word_count} words were found in the document.\n")

	letters = letter_count.keys()
	for letter in letters:
		print(f"The '{letter}' was found {letter_count[letter]} times.")

	print("--- End report ---")

main()