import time
import os
import cipher2login


def save_note(key, notes):
	print "__________________________________________________________________\n"
	while True:
		file_name = raw_input("File Name: ")
		if os.path.isfile("/home/" + str(os.getlogin()) + "/.sec4note/notes/" + file_name):
			print "[!] File exists"

		else:
			break

	file_enc = cipher2login.encript(key, notes)

	file = open("/home/" + str(os.getlogin()) + "/.sec4note/notes/" + file_name, "w")
	file.write(file_enc)
	file.close()

	print "[!] Success"
	time.sleep(0.5)

class Actions:

	def seeAll(self, key, logo):
		while True:
			files = os.listdir("/home/" + str(os.getlogin()) + "/.sec4note/notes/")
			files.append("Exit")

			os.system("clear")

			print logo
			print "\n________________________YOUR_NOTES_____________________________\n"

			line = 0
			for file in files:
				print "        "+str(line)+" |",file
				line += 1
			print "\n__________________________________________________________________"

			try:
				file = int(raw_input("\n        Note ID: "))
			except:
				print "        [!] Invalid type"

			if file > len(files):
				print "        [!] Invalid ID"
				time.sleep(0.5)

			if files[file] == "Exit":
				break

			note_enc = open("/home/" + str(os.getlogin()) + "/.sec4note/notes/" + files[file])
			note_dec = cipher2login.decript(key, note_enc.read())

			os.system("clear")
			print logo
			print "\n______________________"+files[file]+"_________________________\n"
			print note_dec
			print "__________________________________________________________________"

			raw_input("\nPress Enter to see notes list..")
	def addNew(self, key, logo):
		write = True

		while True:
			os.system("clear")
			menu = '''
________________________WRITE_A_NOTE_____________________________


             - Press <ENTER> key to new line.

             - Type "END" to save note.

             - Type "EXIT" to return.

__________________________________________________________________
			'''

			print logo
			print menu

			line = 1
			note = ""
			while True:
				noten = raw_input(str(line)+" | ")

				if noten == "END":
					save_note(key, note)
					break

				elif noten == "EXIT":
					write = False
					break

				note += str(line) + " | " + noten + "\n"
				line += 1

			if write == False:
				break
				time.sleep(2)




