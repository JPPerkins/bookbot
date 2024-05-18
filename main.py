def main():
	book_path = "books/frankenstein.txt"
	print(f"--- Begin report of {book_path} ---")

	text = read_book_from_file(book_path)
	
	num_words = count_words(text) 
	print(f"{num_words} words found in the document")

	sorted_letters = count_letters(text)
	for entry in sorted_letters:
		print(f"The '{entry["character"]}' character was found {entry["count"]} times")
	print("--- End report ---")


def count_words(text):
	seperated_words = text.split()
	return len(seperated_words)
	

def count_letters(text):
	counted_letters = {}
	final_result = []
	lowered_text = text.lower()

	for character in lowered_text:
		if character.isalpha():
			if character in counted_letters:
				counted_letters[character] += 1
			else:
				counted_letters[character] = 1

	for character in counted_letters:
		new_dictionary = {"character": "", "count": 0}
		new_dictionary["character"] = character
		new_dictionary["count"] = counted_letters[character]
		final_result.append(new_dictionary)

	final_result.sort(reverse=True, key=sort_on)
	return final_result


def sort_on(dict):
	return dict["count"]


def read_book_from_file(book_path):
	with open(book_path) as f:
		return f.read()

main()