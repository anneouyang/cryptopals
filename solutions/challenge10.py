import base64
from Crypto.Cipher import AES
import challenge2

key = b'YELLOW SUBMARINE'
block_size = 16
cipher = AES.new(key, AES.MODE_ECB)
iv = bytes([0] * block_size)

def getBlocks(s):
	return [s[i * block_size : (i + 1) * block_size] for i in range(len(s) // block_size)]

def CBCEncrypt(s):
	blocks = getBlocks(s)
	cipher_text = b''
	prv = iv
	for i in range(len(blocks)):
		curblock = cipher.encrypt(challenge2.fixedXor(blocks[i], prv))
		cipher_text += curblock
		prv = curblock
	return cipher_text

def CBCDecrypt(s):
	blocks = getBlocks(s)
	plain_text = b''
	prv = iv
	for i in range(len(blocks)):
		curblock = challenge2.fixedXor(cipher.decrypt(blocks[i]), prv)
		plain_text += curblock
		prv = blocks[i]
	return plain_text

def main():
	f = open('data10.txt', 'r')
	s = base64.b64decode(f.read())
	print(CBCDecrypt(s).decode())

if __name__ == '__main__':
	main()