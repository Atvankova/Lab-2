import csv
import random

DATASET_PATH = 'books-en.csv'
OUT_PATH_BIBLIOGRAPHY = 'bibliography.txt'


def load_books(dataset):
    books = []
    reader = csv.DictReader(dataset, delimiter=';', quotechar='"')
    for row in reader:
        books.append(row)
    return books


def get_random_books(books, num_books=20):
    return random.sample(books, min(num_books, len(books)))


if __name__ == '__main__':
    with open(DATASET_PATH) as dataset:
        books = load_books(dataset)
        random_books = get_random_books(books)
        bibliography_entries = []
        for book in random_books:
            entry = f"{book['Book-Author']}. {book['Book-Title']} - {book['Year-Of-Publication']}"
            bibliography_entries.append(entry)
        with open(OUT_PATH_BIBLIOGRAPHY, 'w') as out_file:
            for i, entry in enumerate(bibliography_entries, start=1):
                out_file.write(f"{i}. {entry}\n")