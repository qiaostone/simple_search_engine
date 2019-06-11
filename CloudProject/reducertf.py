#!/usr/bin/env python

# import modules
from itertools import groupby
from operator import itemgetter
import sys
import json

# 'file' in this case is STDIN
def read_mapper_output(file, separator='\t'):
    # Go through each line
    for line in file:
        # Strip out the separator character
        yield line.rstrip().split(separator, 2)

def main(separator='\t'):
    # Read the data using read_mapper_output
    data = read_mapper_output(sys.stdin, separator=separator)
    # Group words and counts into 'group'
    #   Since MapReduce is a distributed process, each word
    #   may have multiple counts. 'group' will have all counts
    #   which can be retrieved using the word as the key.

    word_dic = {}
    for line in data:
        word_name = line[0]
        word_pagenumber = line[1].strip("\t").split(":")[0]

        record = word_dic.get(word_name.strip())
        if record == None:
            word_dic[word_name] = {word_pagenumber:1}
        else:
            page_record = record.get(word_pagenumber.strip())
            if page_record == None:
                record[word_pagenumber] = 1
            else:
                record[word_pagenumber] += 1

    # with open("count.json","w") as f:
    #     json.dump(word_dic,f)

    for key in word_dic:
        print "%s%s%s" % (key, separator, word_dic[key])

if __name__ == "__main__":
    main()