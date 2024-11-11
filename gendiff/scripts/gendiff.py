import argparse
import json


def load_json(filepath):
    with open(filepath, 'r') as file:
        return json.load(file)


def main():
    parser = argparse.ArgumentParser(description='Compares two configuration files and shows a difference.')

    parser.add_argument('first_file', help='The path to the first file to compare.')
    parser.add_argument('second_file', help='The path to the second file to compare.')
    parser.add_argument('-f', '--format', default='plain', help='set format of output (default: plain)')

    args = parser.parse_args()

    data1 = load_json(args.first_file)
    data2 = load_json(args.second_file)

    print(f"Comparing '{args.first_file}' and '{args.second_file}' with format '{args.format}'.")
    print("Data from first file:", data1)
    print("Data from second file:", data2)


if __name__ == "__main__":
    main()
