import binascii

def fixedXor(s1, s2):
	try:
		s1 = binascii.unhexlify(s1)
	except:
		pass
	try:
		s2 = binascii.unhexlify(s2)
	except:
		pass
	s = ("".join(chr(x ^ y) for x, y in zip(s1, s2))).encode()
	return s

def main():
	s1 = '1c0111001f010100061a024b53535009181c'
	s2 = '686974207468652062756c6c277320657965'
	print((fixedXor(s1, s2)).hex())

if __name__== "__main__":
	main()