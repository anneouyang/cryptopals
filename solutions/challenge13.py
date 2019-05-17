from Crypto.Util.Padding import pad, unpad
from Crypto.Cipher import AES
import challenge11

block_size = 16
key = challenge11.getRandomBytes(16)
cipher = AES.new(key, AES.MODE_ECB)

def kvParse(s):
	s = s.split('&')
	d = {}
	for p in s:
		p = p.split('=')
		d[p[0]] = p[1]
	return d

def profileFor(email):
	email = email.replace('&', '').replace('=', '')
	return {'email' : email, 'uid' : '10', 'role' : 'user'}

def encodeProfile(d):
	ret = ""
	for dictkey in d:
		ret += (dictkey + "=" + d[dictkey] + "&")
	return ret[:-1]

def encryptProfile(email):
	return cipher.encrypt(pad(encodeProfile(profileFor(email)).encode(), block_size))

def decryptProfile(s):
	s = cipher.decrypt(s)
	return (s.decode().strip())

def main():
	print(decryptProfile(encryptProfile("foo&==fo&&o@bar.com")))

if __name__ == '__main__':
	main()