import sys
import itertools
from collections import Counter
from ic import index_coinc
from xor import string_xor
from toHex import base64_to_hex
from fromHex import hex_to_ascii

def combine_factors(val, lst):
    for i in range (2, val):
        if val % i == 0:
            lst.append(i)
    return lst

def guess_keys(val, line):
    key = ''
    result = []
    keys = [[] for i in range(val)]
    lst = list(line)
    lst = [lst[i:i+val] for i in range(0, len(lst), val)]
    for i in range(val):
        if (i >= len(lst[i])):
            break
        # ignore last row 
        col = [row[i] for row in lst[:-1]]
        c = Counter(col)
        for j in range(4):
            keys[i].append(c.most_common(4)[j][0])

    keys = list(itertools.product(*keys))

    for key in keys:
        for char in ['e', 't', 'a', 'o']:
            result.append(string_xor(key, char))
    return result

def multi_xor():
    if len(sys.argv) != 2:
        print("Please enter a single text file")
        return

    infile = open(sys.argv[1], 'r')

    line_num = 0
    lst = []

    for line in infile:
        line_num+=1
        #line = line.rstrip()
        line = hex_to_ascii(base64_to_hex(line.rstrip()))
        
        for i in range(0, len(line)-5):
            repeat = line.find(line[i:i+3], i+3)
            if repeat > 0:
                offset = line.find(line[i:i+3], i+3) - i
                lst = combine_factors(offset, lst)

        c = Counter(lst)
        for x in c.most_common(5):
            if (x <= 3):
                continue;
            keys = guess_keys(x[0], line)

            for key in keys:
                newline = string_xor(line, key)
                ic = index_coinc(newline)
                if ic > .95 and ic < 2:
                    print("KEY: " + key)
                    print("Decoded? \n" + newline)
                    print("IC: " + str(ic))
                    print()

if __name__ == '__main__':
    multi_xor()
