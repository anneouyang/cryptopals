from Crypto.Cipher import AES
import base64

def main():
	f = open('data7.txt', 'r')
	s = base64.b64decode(f.read())
	key = b'YELLOW SUBMARINE'
	cipher = AES.new(key, AES.MODE_ECB)
	print(cipher.decrypt(s).decode())

if __name__== "__main__":
	main()