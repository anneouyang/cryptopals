from Crypto.Util.Padding import pad, unpad
from Crypto.Cipher import AES

def main():
	s = b'YELLOW SUBMARINE'
	block_size = 20
	print(pad(s, block_size))

if __name__== "__main__":
	main()