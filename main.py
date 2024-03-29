def main():
	book_path = "books/frankenstein.txt"
	book_text = get_book_text(book_path)
	print(book_text)

	frankenstein_words = word_count(book_text)
	print(f"There are {frankenstein_words} words in frankenstein.")


# Getting Text
def get_book_text(path):
	with open(path) as f:
		return f.read()


# Counting Words
def word_count(text):
	words = text.split()

	count = 0
	for word in words:
		count += 1
	return count


main()