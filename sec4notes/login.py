import pwinput
import os
import cipher2login

def new_account():

	print "\n[!] Create a new account\n"
	while True:
		name = str(os.getlogin())
		passw = pwinput.pwinput("Create a password: ")
		passw_conf = pwinput.pwinput("Confirm yout password: ")

		if passw != passw_conf:
			print "[!] Passwords dont match"
		else:
			break

	os.mkdir("/home/" + str(os.getlogin()) + "/.sec4note/")
	os.mkdir("/home/" + str(os.getlogin()) + "/.sec4note/notes/")

	print "[INFO] create dir /home/" + str(os.getlogin()) + "/.sec4note/"

	key = cipher2login.gen_pass(passw)
	login = cipher2login.encript(key, name)

	file = open("/home/" + str(os.getlogin()) + "/.sec4note/auth", "w")
	file.write(login)
	file.close()

	print "[!] auth file as been create restart the program to login"
	exit(0)


def check_1_run():

	user_exist = os.path.isfile("/home/" + str(os.getlogin()) + "/.sec4note/auth")

	if user_exist:
		user_exists = True
	else:
		user_exists = False
		while True:
			install = raw_input('[!] auth file dont found\nCreate a new account ? [Y/n]')

			if install == "Y" or install == "y" or install == "":
				new_account()

			elif install == "n" or install == "Y":
				exit(0)

			else:
				print "[!] Invalid option"

	return user_exists

class Login:

	def check(self):
		check_1_run()
		ok = False

		for attemp in range(3):
			user = str(os.getlogin())
			passw = pwinput.pwinput("Pass: ", mask="*")

			file = open("/home/" + str(os.getlogin()) + "/.sec4note/auth")
			enc_data = file.read()

			key = cipher2login.gen_pass(passw)
			check = cipher2login.decript(key, enc_data)

			if check == user:
				ok = True
				break
			else:
				print "[!] Invalid user or password"



		if ok == False:
			exit(0)
		else:
			return key
