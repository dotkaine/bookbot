def main():
    book_path = "books/frankenstein.txt"
    book_content = get_book(book_path)
    word_count = get_word_count(book_content)
    letter_dict = get_letter_count(book_content)
    sorted_letter_list = sort_letter_dict_to_list(letter_dict)

    print("--- Report of frankenstein ---")
    print(f"{word_count} words found in the document")
    for s in sorted_letter_list:
        print(f"The '{s['name']}' character was found {s['num']} times")

def get_book(path):
    with open(path) as f:
        return f.read()

def get_word_count(text):
    count = text.split()
    return len(count)

def get_letter_count(text):
    each_letter = {}
    lower_text = text.lower()
    for c in lower_text:
        if c.isalpha():
            if c not in each_letter:
                each_letter[c] = 1
            each_letter[c] += 1 
    return each_letter

def sort_letter_dict_to_list(letters):
    letter_count_list = []
    for l in letters:
        letter_count_list.append({"name": l, "num": letters[l]})
    letter_count_list.sort(key=sort_on)
    return letter_count_list

def sort_on(book_dict):
    return book_dict["num"]

main()