import os
import argparse
from collections import ChainMap

def main():
    app_defaults = {'username':'admin', 'password':'admin'}

    parser = argparse.ArgumentParser(
            description = "This program demonstrates the power of ChainMap and argparse",
            epilog = "have a nice day!"
            )
    parser.add_argument('-u', '--username')
    parser.add_argument('-p', '--password')
    args = parser.parse_args()
    command_line_arguments = {key:value for key, value in vars(args).items() if value}
    chain = ChainMap(command_line_arguments, os.environ, app_defaults)
    print(chain['username'])

if __name__ == "__main__":
    main()
