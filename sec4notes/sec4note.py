import login
import time
import os, notes
import change_cred

logo = '''

 .M"""bgd                              `7MN.   `7MF'         mm
,MI    "Y                                MMN.    M           MM
`MMb.      .gP"Ya   ,p6"bo       ,AM     M YMb   M  ,pW"Wq.mmMMmm .gP"Ya
  `YMMNq. ,M'   Yb 6M'  OO      AVMM     M  `MN. M 6W'   `Wb MM  ,M'   Yb
.     `MM 8M"""""" 8M         ,W' MM     M   `MM.M 8M     M8 MM  8M""""""
Mb     dM YM.    , YM.    , ,W'   MM     M     YMM YA.   ,A9 MM  YM.    ,
P"Ybmmd"   `Mbmmd'  YMbmd'  AmmmmmMMmm .JML.    YM  `Ybmd9'  `Mbmo`Mbmmd'
                                  MM    By: https://github.com/them3x
                                  MM

'''

os.system('clear')
print logo
key = login.Login().check()


menu = '''
_______________________________MENU_______________________________
              ______________________________________
             |                    |                 |
             | 1) Sholl all notes | 2) Write a note |
             |____________________|_________________|
                |                    |          |
                | 3) Change password | 4) Exit  |
                |____________________|__________|
__________________________________________________________________

'''



while True:
	os.system("clear")
	print logo
	print menu
	chose = str(raw_input("        Type: "))

	if chose == "1":
		notes.Actions().seeAll(key, logo)

	elif chose == "2":
		notes.Actions().addNew(key, logo)

	elif chose == "3":
		key = change_cred.Change().password(key)

	elif chose == "4":
		exit(0)

	else:
		print "        [!] Invalid option"
		time.sleep(0.5)

