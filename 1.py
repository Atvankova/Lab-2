import csv

DATASET_PATH = 'books-en.csv'


def get_title(dataset):
    dataset.seek(0)
    title = next(dataset)
    title = title.split(';')
    title = [col.strip() for col in title]
    return title


def get_object(line, title):
    reader = csv.DictReader([line], title, delimiter=';', quotechar='"')
    res = next(reader)
    return res


def filter_title(dataset, title):
    res = 0
    for line in dataset:
        obj = get_object(line, title)
        book_title_value = obj['Book-Title']
        if len(book_title_value) > 30:
            res += 1
    dataset.seek(0)
    return res


if __name__ == '__main__':
    with open(DATASET_PATH) as dataset:
        title = get_title(dataset)
        print(filter_title(dataset, title))
