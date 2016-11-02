import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-w', required=True)
    args = vars(parser.parse_args())
    words = args['w'].split()
    count_dict = {}
    for word in words:
        if word in count_dict:
            count_dict[word] += 1
        else:
            count_dict[word] = 1
    print(count_dict)


if __name__ == "__main__":
    main()
