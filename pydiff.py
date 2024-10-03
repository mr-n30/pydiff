#!/usr/bin/env python3
import argparse

def find_new_entries(file_a, file_b, new_file):
    # Read content from file-a.txt
    with open(file_a, 'r') as fa:
        content_a = set(fa.read().splitlines())

    # Read content from file-b.txt
    with open(file_b, 'r') as fb:
        content_b = set(fb.read().splitlines())

    # Find new entries in file-a.txt that are not in file-b.txt
    new_entries = content_a - content_b

    if new_entries:
        # Append new entries to new.txt
        with open(new_file, 'a') as nf:
            for entry in new_entries:
                nf.write(entry + '\n')

        # Append new entries to file-b.txt
        with open(file_b, 'a') as fb:
            for entry in new_entries:
                fb.write(entry + '\n')

        print(f"Found {len(new_entries)} new entries. Updated '{new_file}' and '{file_b}'.")
    else:
        print("No new entries found.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Find new entries in file A not in file B.')
    parser.add_argument('-a', required=True, help='Path to file-a.txt')
    parser.add_argument('-b', required=True, help='Path to file-b.txt')
    parser.add_argument('-o', required=True, help='Path to new.txt')

    args = parser.parse_args()

    find_new_entries(args.a, args.b, args.o)
