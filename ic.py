# English IC is 1.73
# (with normalizing coefficient of 26) 
# return IC of input
def index_coinc(text):

    # flatten text
    text = ''.join([text.lower() for x in text.split() if x.isalpha()])

    total = len(text)
    if (total <= 1):
        return 0

    # count letters in input
    letters = map(chr, range(ord('a'), ord('z')+1))

    # not exactly a count, represents numerator in iC formula
    count = 0.0
    for c in letters:
        count += (text.count(c) * (text.count(c) - 1))

    return float('%.4f'%(26 * (count / (total * (total-1)))))

if __name__ == '__main__':
    e don't try to fade this\n"))
