
class dashboard():



	def __init__(__self, key, aes, os, dir_base, clear, logo):

		def edit_passwords(key, aes, os, dir_base):
			if os.path.isfile(dir_base + '.enc') == False:
				file = open(dir_base + '.enc', 'w')
				file.close()
			else:
				with open(dir_base + '.enc', 'rb') as f:
					enc_file = f.read()

				ascii_data = str(aes.decript(key, enc_file)).replace("b\'", "")

				with open(dir_base + '.enc', 'w') as f:
					data = ascii_data[:-1].replace('\\n', '--BREAK-LINE--')
					data = data.replace('--BREAK-LINE--', '\n')
					f.write(data)

			os.system('nano ' + dir_base + '.enc -l')

			if os.path.isfile(dir_base + '.enc.save'):
				os.remove(dir_base + '.enc.save')

			with open(dir_base + '.enc') as f:
				ascii_file = f.read()

			data = aes.encript(key, ascii_file)

			with open(dir_base + '.enc', 'wb') as f:
				f.write(data)


		opt = """
1) Show my files
2) Exit
		"""

		while True:
			clear()
			print(logo)

			print(opt)
			select = input('Type >')

			if select == '2':
				exit()

			elif select == '1':
				edit_passwords(key, aes, os, dir_base)

