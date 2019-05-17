import base64
from Crypto.Cipher import AES
import challenge11
from Crypto.Util.Padding import pad, unpad

unknownString = b'Um9sbGluJyBpbiBteSA1LjAKV2l0aCBteSByYWctdG9wIGRvd24gc28gbXkgaGFpciBjYW4gYmxvdwpUaGUgZ2lybGllcyBvbiBzdGFuZGJ5IHdhdmluZyBqdXN0IHRvIHNheSBoaQpEaWQgeW91IHN0b3A/IE5vLCBJIGp1c3QgZHJvdmUgYnkK'
unknownString = base64.b64decode(unknownString)
block_size = 16
key = challenge11.getRandomBytes(16)
cipher = AES.new(key, AES.MODE_ECB)

def ECBEncrypt(s):
	s2 = pad(s + unknownString, block_size)
	return cipher.encrypt(s2)

def getBlockSize():
	ss = b''
	ini_len = len(ECBEncrypt(ss))
	while True:
		ss += b'A'
		new_len = len(ECBEncrypt(ss))
		if(new_len != ini_len):
			return new_len - ini_len

def checkECB():
	if challenge11.detectAESType(ECBEncrypt(challenge11.getRandomBytes(block_size) * 4)) == "ECB":
		return True
	return False

def findUnknownString():
	ret = b''
	known = b''
	d = {}
	while True:
		prefix = (b'A') * (block_size - 1 - len(known) % computed_block_size)
		for i in range(256):
			pos = ECBEncrypt(prefix + known + str(chr(i)).encode())
			d[pos[0:len(prefix) + len(known) + 1]] = str(chr(i)).encode()
		act = ECBEncrypt(prefix)
		if(act[0:len(prefix) + len(known) + 1] in d):
			known += d[act[:len(prefix) + len(known) + 1]]
		else:
			return known

def main():
	global computed_block_size
	computed_block_size = getBlockSize()
	if checkECB():
		print(findUnknownString())
	else:
		print("Not ECB mode")

if __name__ == '__main__':
	main()