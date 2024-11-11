import argparse


def main():
    parser = argparse.ArgumentParser(description='Compares two configuration files and shows a difference.')

    parser.add_argument('first_file', help='The path to the first file to compare.')
    parser.add_argument('second_file', help='The path to the second file to compare.')

    parser.add_argument('-f', '--format', default='plain', help='set format of output (default: plain)')

    args = parser.parse_args()

    print(f"Comparing '{args.first_file}' and '{args.second_file}' with format '{args.format}'.")


if __name__ == "__main__":
    main()
