import pyaes
import hashlib



def gen_pass(key):
	result = hashlib.md5(key).hexdigest()
	result = str(result.encode('BASE64')).encode('BASE64')

	return result[:32]


def encript(key, data):
	aes = pyaes.AESModeOfOperationCTR(key)
	crypto_data = aes.encrypt(data)

	return crypto_data

def decript(key, data):
	aes = pyaes.AESModeOfOperationCTR(key)
	decrypt_data = aes.decrypt(data)

	return decrypt_data
