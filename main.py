import sys
from stats import get_num_words, get_char_count, sort_count_descending

def get_book_text(path: str):
    with open(path) as f:
        content = f.read()
        return content

def main():
    args = sys.argv
    if len(args) != 2:
        print('Usage: python3 main.py <path_to_book>')
        sys.exit(1)
    file_path = args[1]
    try:
        content = get_book_text(file_path)
    except Exception as e:
        print(f'Unable to open file {file_path}: {str(e)}')
        return
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
