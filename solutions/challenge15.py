def pkcs7unpad(s):
	len = int(s[-1])
	if len == 0 or s[-len:] != (bytes([len]) * len):
		raise ValueError("Invalid padding")
	return s[:-len]

def main():

	try:
		print(pkcs7unpad(b'ICE ICE BABY\x04\x04\x04\x04'))
	except:
		pass

	try:
		print(pkcs7unpad(b'ICE ICE BABY\x05\x05\x05\x05'))
	except:
		pass

	try:
		print(pkcs7unpad(b'ICE ICE BABY\x01\x02\x03\x04'))
	except:
		pass

if __name__ == '__main__':
	main()