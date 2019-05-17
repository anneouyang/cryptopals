import binascii

def main():
	f = open('data8.txt', 'r')
	block_size = 16
	pos = []
	for s in f:
		if s[-1] == '\n':
			s = s[:-1]
		blocks = [s[i * block_size : (i + 1) * block_size] for i in range(len(s) // block_size)]
		pos.append((s, len(blocks) - len(set(blocks))))
	pos.sort(key = lambda a : a[1], reverse = True)
	print(pos[0])

if __name__=="__main__":
	main()