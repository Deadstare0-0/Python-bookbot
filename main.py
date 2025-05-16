def main():
    book_path = "books/frankenstein.txt"
    count = count_words(book_path)
    print(f"{count} words found in the document")

def count_words(path):
    with open(path) as f:
        temp = f.read()
    count = len(temp.split())
    return count

main()