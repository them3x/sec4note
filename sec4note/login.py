
def login(dir_base, os, getpass, aes, install, menu, clear, logo):


	try:
		file = open(dir_base + '.auth', 'rb')
		enc_file = file.read()
		file.close()
	except:
		install.installer(dir_base, os, getpass, aes)

	clear()
	print (logo)

	x = 0
	success = False
	while x != 5:
		password = aes.gen_pass(getpass.getpass('Password: '))
		dec_file = aes.decript(password, enc_file)

		try:
			if dec_file.decode() == '1':
				success = True
				break
		except:
			None
		x += 1

	if success:
		menu.dashboard(password, aes, os, dir_base, clear, logo)
