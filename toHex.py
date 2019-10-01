import codecs
import base64

def ascii_to_hex(text):
    return ''.join('{0:02x}'.format(ord(c)) for c in text)

def base64_to_hex(x):
    return codecs.encode(codecs.decode( bytes(x, 'utf-8'), 'base64'), 'hex').decode().rstrip() # python 3?

if __name__ == '__main__':
    print(ascii_to_hex("Hello World"))
    print(base64_to_hex("YW55IGNhcm5hbCBwbGVhc3VyZS4="))
