# import
import os, sys, time
# Color
green="\033[92m"
yellow="\033[93m"
red="\033[91m"
blue="\033[96m"
white="\033[97m"
# Banner
def Banner():
  os.system("clear")
  os.system("figlet -f mono9 Hacking tools | lolcat ")
  os.system("cat Banner.txt | lolcat")
  print(red + "\n\nAuthor    " + blue + ": " + white + "Pound")
  print(red + "age       " + blue + ": " + white + "14\n")
  os.system("cat Banner.txt | lolcat")
  print(white + "\n\n[" + red + "1" + white + "]      " + blue + ": " + white + "Sqlmap")
  print(white + "\n[" + red + "2" + white + "]      " + blue + ": " + white + "Metasploit")
  print(white + "\n[" + red + "3" + white + "]      " + blue + ": " + white + "Nmap")
  print(white + "\n[" + red + "4" + white + "]      " + blue + ": " + white + "Nikto")
  print(white + "\n[" + red + "5" + white + "]      " + blue + ": " + white + "Exiftool")
  print(white + "\n[" + red + "0" + white + "]      " + blue + ": " + white + "Exit")
# Sqlmap
def Sqlmap(): # ใช้เจาะระบบเว็บไซต์ที่มีช่องโหว่Sql injection by injection
  os.system("clear")
  os.system("figlet -f mono9 Sqlmap | lolcat")
  os.system("apt update && apt upgrade && pip install sqlmap")
  os.system("clear")
  os.system("cat Banner_Sqlmap.txt | lolcat")
  sys.exit()
# Metasploit
def Metasploit(): # ใช้สร้างPayloadได้เเละสามารถใช้เจาะระบบได้ด้วย
  os.system("clear")
  os.system("figlet -f mono9 Metasploit | lolcat")
  os.system("apt update && apt upgrade && apt install wget -y && apt install postgresql -y && apt install openssh -y && apt install curl -y")
  os.syatem("cd ~")
  os.system("wget https://raw.githubusercontent.com/gushmazuko/metasploit_in_termux/master/metasploit.sh")
  os.system("chmod +x metasploit.sh")
  os.system("./metasploit.sh")
  os.system("cd ~/Hacking_Tools")
  os.system("mv m ~/../usr/bin")
  os.system("chmod 777 ~/../usr/bin/m")
  os.system("mv Metasploit.py $HOME")
  os.system("clear")
  os.system("cat Hacking_Tools/Banner_Metasploit.txt | lolcat")
  sys.exit()
# Nmap
def Nmap(): # ใช้สเเกนระบบเครือข่าย
  os.system("clear")
  os.system("figlet -f mono9 Nmap | lolcat")
  os.system("apt update && apt upgrade && apt install nmap -y")
  os.system("clear")
  os.system("cat Banner_Nmap.txt | lolcat")
  sys.exit()
# Nikto
def Nikto(): # ใช้สเเกนหาช่องโหว่เว็บไซต์
  os.system("clear")
  os.system("figlet -f mono9 Nikto | lolcat")
  os.system("apt update && apt upgrade && apt install perl -y && apt install git -y")
  os.system("git clone https://github.com/sullo/nikto.git")
  os.system("mv nikto $HOME")
  os.system("cd Data")
  os.system("mv nikto ~/../usr/bin")
  os.system("chmod 777 ~/../usr/bin/nikto")
  os.system("clear")
  os.system("cat Banner_Nikto.txt | lolcat")
  sys.exit()
# exiftool
def Exiftool(): # ใช้ดูดข้อมูลของรูปภาพรวมถึงที่อยู่ของรูปภาพที่ถ่ายตรง100%
  os.system("clear")
  os.system("figlet -f mono9 Exiftool | lolcat")
  os.system("apt update -y && apt upgrade -y && apt install exiftool -y")
  os.system("clear")
  os.system("mv e ~/../usr/bin")
  os.system("chmod 777 ~/../usr/bin/e")
  os.system("mv exiftool.py $HOME")
  os.system("cat Banner_Exiftool.txt | lolcat")
  sys.exit()
# Home 
Banner()
Select = input(white + "\n[" + red + "Install" + white + "]        " + blue + ": " + white + "")
if Select == "1":
  Sqlmap()
elif Select == "2":
  Metasploit()
elif Select == "3":
  Nmap()
elif Select == "4":
  Nikto()
elif Select == "5":
  Exiftool()
elif Select == "0":
  print(white + "\n\t[" + red + "Thanks" + white + "]")
  sys.exit()
else:
  print(white + "\n\t[" + red + "Errors!" + white + "]")
  sys.exit()
