import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    re.search(r"<iframe(.)*><\/iframe>",s)
    url_pattern = re.search(r"(http(s)*:\/\/(www\.)*youtube\.com\/embed\/[a-zA-Z0-9]+)",s)
    if url_pattern:
        get_pattern = url_pattern.groups()
        # return ("https://youtu.be/"+get_pattern[3])
        print(get_pattern)
if __name__ == "__main__":
    main()
