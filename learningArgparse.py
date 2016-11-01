import argparse

def get_args():
    """"""
    parser = argparse.ArgumentParser(
            description="Yo check dis description",
            epilog="Usage: TODO",
            )
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-x', '--execute', action="store", help='Help text for option X')
    group.add_argument('-y', help='Help got y', type=int)
    parser.add_argument('-z', help='Help for z', default=False)
    print(parser.parse_args())

if __name__ == "__main__":
    get_args()
