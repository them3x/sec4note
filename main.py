import login
import install
import os
import platform
import getpass
import aes
import menu


if platform.system() == 'Linux':
	dir_base = '/home/' + os.getlogin() + '/.genpass/'

	def clear():
		os.system('clear')


clear()

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
print (logo)



login.login(dir_base, os, getpass, aes, install, menu, clear, logo)
