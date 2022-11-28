
class dashboard():



	def __init__(__self, key, aes, os, dir_base, clear, logo):

		def open_file(key, aes, os, dir_base):
			if os.path.isfile(dir_base) == False:
				file = open(dir_base, 'w')
				file.close()
			else:
				with open(dir_base, 'rb') as f:
					enc_file = f.read()

				ascii_data = str(aes.decript(key, enc_file)).replace("b\'", "")

				with open(dir_base, 'w') as f:
					data = ascii_data[:-1].replace('\\n', '--BREAK-LINE--')
					data = data.replace('--BREAK-LINE--', '\n')
					f.write(data)

			os.system('nano ' + dir_base + ' -l')

			if os.path.isfile(dir_base + '.save'):
				os.remove(dir_base + '.save')

			with open(dir_base) as f:
				ascii_file = f.read()

			data = aes.encript(key, ascii_file)

			with open(dir_base, 'wb') as f:
				f.write(data)


		help = """

_________________HELP___________________
                                        |
 Type > new <Name file>   - Crete file  |
 Type > del <NUM file>    - Delete file |
 Press: CTRL + C          - Quit        |
________________________________________|

"""

		seehelp = False

		while True:
			clear()
			print(logo)

			files = os.listdir(dir_base)
			files.remove('.auth')
			count = 1

			if seehelp == True:
				seehelp = False
				opt = help
			else:
				opt = "Type > help - See tutorial\n\n"

			for i in files:
				if count == 1:
					opt = opt + str(count) + ") " + i + '\n'
					count += 1
					continue

				opt = opt + str(count) + ") " + i + "\n"
				count += 1

			print(opt)
			select = input('\nType > ')

			try:
				open_file(key, aes, os, dir_base + files[int(select) - 1])
			except:
				try:

					if select.split(' ')[0] == 'new':
						file_name = select.split(' ')[1]
						if os.path.isfile(dir_base + file_name):
							break
						else:
							open_file(key, aes, os, dir_base + file_name)


					elif select.split(' ')[0] == 'del':
						if os.path.isfile(dir_base + files[int(select.split(' ')[1]) - 1]):
							while True:
								chose = input('Remove '+ files[int(select.split(' ')[1]) - 1] + " [s/n] > ")
								if chose.lower() == 's':
									os.remove(dir_base + files[int(select.split(' ')[1]) - 1])
									break

								elif chose.lower() == 'n':
									break
						else:
							print("File dont found")

					elif select.split(' ')[0] == 'help':
						seehelp = True
				except:
					None
