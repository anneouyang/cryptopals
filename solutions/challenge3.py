import binascii

character_frequencies = {
 	'a': .08167, 'b': .01492, 'c': .02782, 'd': .04253,
 	'e': .12702, 'f': .02228, 'g': .02015, 'h': .06094,
 	'i': .06094, 'j': .00153, 'k': .00772, 'l': .04025,
 	'm': .02406, 'n': .06749, 'o': .07507, 'p': .01929,
 	'q': .00095, 'r': .05987, 's': .06327, 't': .09056,
 	'u': .02758, 'v': .00978, 'w': .02360, 'x': .00150,
 	'y': .01974, 'z': .00074, ' ': .13000
 }

def freqScore(s):
	score = 0
	for c in s:
		if c in character_frequencies:
			score += character_frequencies[c]
	return score

def singleByteXor(s):
	li = []
	try:
		s = binascii.unhexlify(s)
	except:
		pass
	for cval in range(256):
		r = "".join(chr(x ^ cval) for x in s)
		score = freqScore(r)
		li.append((r, cval, score))
	li.sort(key = lambda a : a[2], reverse = True)
	return li

def main():
	s = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
	print(singleByteXor(s)[0])

if __name__== "__main__":
	main()