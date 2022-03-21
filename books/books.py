from bs4 import BeautifulSoup as bs
from urllib.request import urlopen
from tqdm.auto import tqdm  
from argparse import ArgumentParser
import json


def get_args():
    parser = ArgumentParser()
    parser.add_argument("--update", action="store_true", help="Update.")
    return parser.parse_args()

def main():
    args = get_args()
    with open('books.json', "r") as f:
        print('# Libros:')
        for book in sorted(json.load(f), key=lambda k: k["title"]):
            print("- {0:}. *{1:}*. {2:}, {3:}.\n".format(book["author"],
                book["title"], book["editorial"], book["year"]))

if __name__ == '__main__':
    main()

