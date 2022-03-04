import pwinput
import os
import cipher2login
import time


def change_notes(password, new_password):

	files = os.listdir("/home/" + str(os.getlogin()) + "/.sec4note/notes/")

	for file in files:
		note = open("/home/" + str(os.getlogin()) + "/.sec4note/notes/" + file)
		note_tmp = open("/home/" + str(os.getlogin()) + "/.sec4note/notes/." + file + ".tmp", "w")

		note_dec = cipher2login.decript(password, note.read())
		note_enc = cipher2login.encript(new_password, note_dec)

		note.close()
		note_tmp.write(note_enc)
		note_tmp.close()

		os.system("mv /home/" + str(os.getlogin()) + "/.sec4note/notes/." + file + ".tmp /home/" + str(os.getlogin()) + "/.sec4note/notes/" + file)

class Change:

	def password(self, password):
		new_password = pwinput.pwinput("        New Password: ", mask="*")
		new_password_c = pwinput.pwinput("        Confirm New Password: ", mask="*")



		if new_password != new_password_c:
			print "        [!] Wrong password"
			time.sleep(0.5)
		else:
			new_password = cipher2login.gen_pass(new_password)

			file = open("/home/" + str(os.getlogin()) + "/.sec4note/auth")
			file_tmp = open("/home/" + str(os.getlogin()) + "/.sec4note/.auth.tmp", "w")
			login = cipher2login.decript(password, file.read())
			file.close()

			if login == str(os.getlogin()):

				login_enc = cipher2login.encript(new_password, login)
				file_tmp.write(login_enc)
				file_tmp.close()

				file_tmp = open("/home/" + str(os.getlogin()) + "/.sec4note/.auth.tmp")
				login = cipher2login.decript(new_password, file_tmp.read())
				file_tmp.close()

				if login != str(os.getlogin()):
					print "        [!888] something unexpected happened"
					os.system("rm /home/" + str(os.getlogin()) + "/.sec4note/.auth.tmp")
					time.sleep(0.5)

				else:
					change_notes(password, new_password)
					print "        [!] Success"
					os.system("mv /home/" + str(os.getlogin()) + "/.sec4note/.auth.tmp /home/" + str(os.getlogin()) + "/.sec4note/auth")
					time.sleep(0.5)
					return new_password

			else:
				print "        [!898] something unexpected happened"
				os.system("rm /home/" + str(os.getlogin()) + "/.sec4note/.auth.tmp")
				time.sleep(0.5)

