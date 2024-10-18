import json
import csv

DATASET_PATH = 'books-en.csv'
OUT_PATH_AUTHOR = 'author.json'


def get_title(dataset):
    dataset.seek(0)
    title = next(dataset).strip().split(';')
    return [col.strip() for col in title]


def get_object(line, title):
    reader = csv.DictReader([line], title, delimiter=';', quotechar='"')
    return next(reader)


def find_by_author_filtered(dataset, title, author):
    results = []
    for line in dataset:
        obj = get_object(line, title)
        author_value = obj['Book-Author']
        price = float(obj['Price'].replace(',', '.')) # нахожу цену
        # (replace чтобы работало с разными типами данных)
        if author_value.lower() == author.lower() and price < 200:
            results.append(obj)
    dataset.seek(0)
    return results


if __name__ == '__main__':
    with open(DATASET_PATH) as dataset:
        title = get_title(dataset)
        author_name = input("Введите имя автора: ")
        res = find_by_author_filtered(dataset, title, author_name)
        with open(OUT_PATH_AUTHOR, 'w') as out:
            json.dump(res, out, ensure_ascii=False, indent=4)
        dataset.seek(0)
        isbns = []
        for line in dataset:
            obj = get_object(line, title)
            isbns.append(obj['ISBN'])