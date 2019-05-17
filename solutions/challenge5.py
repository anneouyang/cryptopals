import binascii

def repeatingKeyXor(s, key):
	s2 = "".join(chr(s[i] ^ key[i % len(key)]) for i in range(len(s)))
	return s2.encode()

def main():
	s = b'''Burning 'em, if you ain't quick and nimble
I go crazy when I hear a cymbal'''
	key = b'ICE'
	print(repeatingKeyXor(s, key).hex())

if __name__== "__main__":
	main()