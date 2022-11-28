import pyaes
import hashlib
import base64

def gen_pass(key):
	result = hashlib.md5(key.encode('utf-8')).hexdigest()
	result = base64.b64encode(bytes(result, 'utf-8')).decode('utf-8')

	return result[:32]


def encript(key, data):
	aes = pyaes.AESModeOfOperationCTR(key.encode())
	crypto_data = aes.encrypt(data)

	return crypto_data

def decript(key, data):
	aes = pyaes.AESModeOfOperationCTR(key.encode())
	decrypt_data = aes.decrypt(data)

	return decrypt_data
