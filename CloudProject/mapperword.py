#!/usr/bin/env python

# Use the sys module
import sys

# 'file' in this case is STDIN
def read_input(file):
    # Split each line into words
    for line in file:
        words_list = line.split(";")

        # tr = temp_sec[2].split(" ")
        # tres = tr[1][1:]
        # # print(res)
        # res = tres.split("?")[0]

        for word_item in words_list:
            if word_item.strip() != "":
                temp_word = word_item.split(",")
                word_name = temp_word[0]
                position = temp_word[1]
            
                yield (word_name.strip(), position.strip())


def main(separator='\t'):
    # Read the data using read_input
    data = read_input(sys.stdin)
    # Process each word returned from read_input
    for word in data:
        # Process each word
        try:
            print '%s%s%s%s%d' % (word[0], separator, word[1], separator, 1)
        except Exception:
            pass


if __name__ == "__main__":
    main()