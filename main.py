def get_book_text(path):
    with open(path) as file:
        file_content = file.read()
        return file_content


def main():
    output = get_book_text('./books/frankenstein.txt')
    print(output)


main()
