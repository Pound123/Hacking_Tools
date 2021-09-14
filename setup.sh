clear
apt update -y && apt upgrade -y && apt install git -y && apt install python -y && pip install lolcat && gem install lolcat && ternux-setup-stroage
mv tools ~/../usr/bin && chmod 777 ~/../usr/bin/tools
mkdir Data && mv nikto Data
clear
cat Banner_install.txt | lolcat
