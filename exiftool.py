# Create by pound
# Code a python
# Color code
green="\033[92m"
yellow="\033[93m"
red="\033[91m"
blue="\033[96m"
white="\033[97m"
# Import
import os, sys, time
# Banner
def Banner():
    os.system("clear")
    os.system("figlet -f mono9 Exiftool | lolcat")
    address = input(white + "\n[" + red + "ที่อยู่รูปภาพ" + white + "]        " + blue + ": " + white + "")
    os.system("exiftool %s"%(address))
    sys.exit()
# Run
Banner()

