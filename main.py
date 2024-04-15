def get_book_text(path):
    with open(path) as file:
        file_content = file.read()
        return file_content


def word_count(text):
    word_count_list = text.split()
    return len(word_count_list)


def char_dict(text):
    chars_dict = {}
    lowered_chars = text.lower()
    for char in lowered_chars:
        if char in chars_dict and char.isalpha():
            chars_dict[char] += 1
        elif char.isalpha():
            chars_dict[char] = 1
    return chars_dict


def dict_to_list_of_dict(char_dict):
    char_list = []
    for char in char_dict:
        char_list.append({"character": char, "count": char_dict[char]})
    return char_list


def sort_on(dict):
    return dict["count"]


def main():
    output = get_book_text('./books/frankenstein.txt')
    book_word_count = word_count(output)
    chars_dict = char_dict(output)
    chars_list = dict_to_list_of_dict(chars_dict)
    chars_list.sort(reverse=True, key=sort_on)
    print('--- Begin report of books/frankenstein.txt ---')
    print(f'{book_word_count} words found in the document\n')
    for char in chars_list:
        print(f"The '{char["character"]}' character was found {
              char["count"]} times")
    print('--- End report ---')
    dict_to_list_of_dict(chars_dict)


main()
