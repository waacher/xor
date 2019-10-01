import codecs

# hex to ascii
def hex_to_ascii(x):
    return bytes.fromhex(x).decode('latin-1')

# hex to base64
def hex_to_64(x):
    return codecs.encode(codecs.decode(x, 'hex'), 'base64').decode().rstrip()

if __name__ == "__main__":
    #print(hex_to_ascii("dd3253b54eb080325a2e5b17ccae5bc241197528aff8897d2f913a5d207ab7019bddec430de8b3ee436bcf28c66bd4ff88c31027603612f35e9983c0beb6206e20949350db4ac095dac6af53d2c46d8a3364c7664a6b6879e08ed2288a7479cf01f68f062bd5aeb1902678716c"))
    #print(hex_to_ascii("48656c6c6f20576f726c64"))
    #print(hex_to_64("10000000000002ae"))
    #print(hex_to_ascii("48656c6c6f20576f726c64"))
    #print(hex_to_ascii("e2889fe29982e2889f4745dae299a52059e29784e2869320e2889f4be299a6e286a8e298bc2ebf27"))
