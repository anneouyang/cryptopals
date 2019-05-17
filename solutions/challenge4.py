import binascii
import challenge3

def main():
	f = open('data4.txt', 'r')
	pos = []
	for s in f:
		if s[-1] == '\n':
			s = s[:-1]
		pos.append(challenge3.singleByteXor(s)[0])
	pos.sort(key = lambda a : a[2], reverse = True)
	print(pos[0])

if __name__== "__main__":
	main()