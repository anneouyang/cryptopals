import binascii
import base64

def hexStringToBase64(s):
	return base64.b64encode(binascii.unhexlify(s))

def main():
	s = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
	s2 = hexStringToBase64(s)
	print(s2)
	print(base64.b64decode(s2).decode())

if __name__== "__main__":
	main()