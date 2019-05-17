from Crypto.Cipher import AES
import random
import secrets
from Crypto.Util.Padding import pad, unpad
import challenge10

key_size = 16
block_size = 16

def getRandomBytes(l):
	return secrets.token_bytes(l)

def encryptionOracle(s):
	key = getRandomBytes(key_size)
	s = getRandomBytes(random.randint(5, 10)) + s + getRandomBytes(random.randint(5, 10))
	s = pad(s, block_size)
	if random.randint(0, 1) == 0:
		print("ECB mode encryption")
		cipher = AES.new(key, AES.MODE_ECB)
		return cipher.encrypt(s)
	else:
		print("CBC mode encryption")
		return challenge10.CBCDecrypt(s)

def detectAESType(encrypted_s):
	blocks = [encrypted_s[i * block_size : (i + 1) * block_size] for i in range(len(encrypted_s) // block_size)]
	if(len(blocks) - len(set(blocks)) > 0):
		return "ECB"
	else:
		return "CBC"

def main():
	for i in range(20):
		enc = encryptionOracle(b'A' * 48)
		print(enc)
		print(detectAESType(enc))

if __name__ == '__main__':
	main()