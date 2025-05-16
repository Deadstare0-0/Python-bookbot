import sys
from stats import count_words
from stats import count_char
from stats import sort_shit


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    word_count = count_words(book_path)
    char_dic = count_char(book_path)
    char_dic = sort_shit(char_dic)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for char, count in char_dic:
        if char.isalpha():
            print(f"{char}: {count}")
    print("============= END ===============")
main()