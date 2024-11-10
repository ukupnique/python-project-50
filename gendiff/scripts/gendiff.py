import argparse

def main():
    parser = argparse.ArgumentParser(description='Compares two configuration files and shows a difference.')
    parser.add_argument('first_file', help='The path to the first file to compare.')
    parser.add_argument('second_file', help='The path to the second file to compare.')
    args = parser.parse_args()
    print(f"Comparing {args.first_file} and {args.second_file}")

if __name__ == "__main__":
    main()
