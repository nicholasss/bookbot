def main():
	book_path = "books/frankenstein.txt"
	book_text = get_book_text(book_path)
	print(book_text)

	frankenstein_words = word_count(book_text)
	print(f"There are {frankenstein_words} words in frankenstein.")

	frankenstein_letters = letter_count(book_text)
	print(frankenstein_letters)

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
			if letter not in count:
				count[letter] = 1
			else:
				count[letter] += 1
	return count


main()