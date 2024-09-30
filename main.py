import os

def main():
    text = get_book_text()
    word_counter = get_num_words(text)
    chars_dict = count_chars(text)
    chars_sorted_list = chars_dict_to_sorted_list(chars_dict)

    print(f"--- Begin report of books/frankenstein.txt ---")
    print(f"{word_counter} words found in the document")
    print()

    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")

    print("--- End report ---")


def get_num_words(text):
    words = text.split()
    return len(words)


def sort_on(d):
    return d["num"]


def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list


def count_chars(text):
    char_count = {}
    for char in text:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count


def get_book_text():
    script_directory = os.path.dirname(os.path.abspath(__file__))
    book_path = os.path.join(script_directory, "books/frankenstein.txt")
    with open(book_path) as f:
        file_contents = f.read()
    return file_contents


if __name__ == "__main__":
    main()



