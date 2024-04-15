def get_book_text(path):
    with open(path) as file:
        file_content = file.read()
        return file_content


def word_count(text):
    word_count_list = text.split()
    return len(word_count_list)


def main():
    output = get_book_text('./books/frankenstein.txt')
    lowered_chars = output.lower()
    chars_dict = {}
    for char in lowered_chars:
        if char in chars_dict and char.isalnum:
            chars_dict[char] += 1
        elif char.isalnum:
            chars_dict[char] = 1
    # book_word_count = word_count(output)
    print(chars_dict)
    # print(f'{book_word_count} words found in the document')


main()
