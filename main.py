from stats import get_num_words, get_char_count, sort_count_descending

def get_book_text(path: str):
    with open(path) as f:
        content = f.read()
        return content

def main():
    file_path = 'books/frankenstein.txt'
    content = get_book_text(file_path)
    num_words = get_num_words(content)
    char_count = get_char_count(content)
    sorted_count = sort_count_descending(char_count)
    print('============ BOOKBOT ============')
    print(f'Analyzing book found at {file_path}...')
    print('----------- Word Count ----------')
    print(f'Found {num_words} total words')
    print('--------- Character Count -------')
    for char in sorted_count:
        print(f'{char['character']}: {char['count']}')
    print('============= END ===============')

main()
