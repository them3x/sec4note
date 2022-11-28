
class installer():

	def __init__(__self, dir_base, os, getpass, aes):

		print('[!] Checking dir \"' + dir_base + '\"')
		if os.path.isdir(dir_base) == False:
			print ("[!] Dir \"" + dir_base + "\": Dont exist")
			try:
				os.mkdir(dir_base)
				print("[!] Dir \"" + dir_base + "\": successfully created")
			except Exception as erro:
				print('[X] Create \"' + dir_base + ' \": Faild')
				print (erro)
				exit(0)

		while True:
			password1 = getpass.getpass('Enter your new password: ')
			password2 = getpass.getpass('Confirm your password: ')

			if password1 == password2:
				break

			print('[X] Passwords dont match')


		print('[!] Genering auth key')
		final_key = aes.gen_pass(password1)

		try:
			file = open(dir_base + '.auth', 'wb')
			file.write(aes.encript(final_key, '1'))
			file.close()


			data = """Hey, im a secure note exemple!

TUTORIAL
If you've never used the text editor, I'll give you some tips

1 - Use arrow keys to move the pointer
2 - Press ENTER to write a new line

When you finish writing something:

2 - Use CTRL + S to save and CTRL + X to close nano and return to menu

Everything you write here is AES 256 encrypted, and the only way to decrypt the file is using your previously created password."""

			file = open(dir_base + '.README', 'wb')
			file.write(aes.encript(final_key, data))
			file.close()

		except Exception as erro:
			try:
				os.remove(dir_base + '.auth')
			except:
				None
			print('[X] Create .auth file: Faild')
			print (erro)
			exit(0)


