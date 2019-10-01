from itertools import cycle

def string_xor(str1, key):
   return ''.join(chr(ord(x) ^ ord(y)) for x, y in zip(str1, cycle(key)))

if __name__ == '__main__':
   #print(string_xor("There are many variations of passages of Lorem Ipsum available, but the majority have suffered alteration in some form, by injected humour, or randomised words which don't look even slightly believable. If you are going to use a passage of Lorem Ipsum, you need to be sure there isn't anything embarrassing hidden in the middle of text. All the Lorem Ipsum generators on the Internet tend to repeat predefined chunks as necessary, making this the first true generator on the Internet. It uses a dictionary of over 200 Latin words, combined with a handful of model sentence structures, to generate Lorem Ipsum which looks reasonable. The generated Lorem Ipsum is therefore always free from repetition, injected humour, or non-characteristic words etc.", "KEY"))

   #print(string_xor("One, two, three and to the fo'", "6179E6805A"))
