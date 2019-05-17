import binascii
import base64
import challenge3
import challenge5

def hammingDistance(s1, s2):
	return sum([bin(s1[i] ^ s2[i]).count('1') for i in range(len(s1))])

def breakRepeatedXor(s):
	key_sizes = []
	for sz in range(2, 41):
		tmp = []
		for i in range(len(s) // sz - 1):
			tmp.append(hammingDistance(s[i * sz : (i + 1) * sz], s[(i + 1) * sz : (i + 2) * sz]) / sz)
		key_sizes.append((sum(tmp) / len(tmp), sz))
	key_sizes.sort(key = lambda a : a[0])
	KEYSIZE = key_sizes[0][1]
	
	blocks = [[] for i in range(KEYSIZE)]
	for i in range(len(s)):
		blocks[i % KEYSIZE].append(s[i])
	
	key = ""
	for block in blocks:
		key_char = challenge3.singleByteXor(block)[0]
		key += chr(key_char[1])
	return key.encode()


def main():
	f = open('data6.txt', 'r')
	s = base64.b64decode(f.read())

	# s1 = b'this is a test'
	# s2 = b'wokka wokka!!!'
	# print(hammingDistance(s1, s2))

	key = breakRepeatedXor(s)
	print("The key is", key, "\n")
	print(challenge5.repeatingKeyXor(s, key).decode())

if __name__== "__main__":
	main()