import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    re.search(r"<iframe(.)*><\/iframe>",s)
        url_pattern = re.search("(http(s)*\:\/\/(www\.)*youtube\.com\/embed\/[a-z_A-Z_0-9]+)",s)
        if url_pattern:


if __name__ == "__main__":
    main()
