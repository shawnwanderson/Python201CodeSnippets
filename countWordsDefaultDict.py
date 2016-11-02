from collections import defaultdict
import argparse

default_sentence = "hey checkout this cool default sentence"

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-w")
    args = vars(parser.parse_args())
    sentence = args['w'] if args['w'] else default_sentence
    words = sentence.split()

    d = defaultdict(int)
    for word in words:
        d[word] += 1

    print(d)

if __name__ == "__main__":
    main()
