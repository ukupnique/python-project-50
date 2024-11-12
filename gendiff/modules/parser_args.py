import argparse


def parser_args():
    parser = argparse.ArgumentParser(description='Compares two configuration files and shows a difference.')

    parser.add_argument('first_file', help='The path to the first file to compare.')
    parser.add_argument('second_file', help='The path to the second file to compare.')
    parser.add_argument('-f', '--format', default='stylish', choices=['stylish', 'plain', 'json'],
                        help='set format of output (default: plain)')

    args = parser.parse_args()

    return args
