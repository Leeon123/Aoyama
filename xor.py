import sys
import base64 as b64
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

def main():
    if len(sys.argv) != 4 :
        print("Usage: "+sys.argv[0]+" key string enc/dec")
        sys.exit(1)
    if sys.argv[3] == "enc":
        string = xor_enc(sys.argv[2],sys.argv[1])
        print("Encoded string: "+string)
    if sys.argv[3] == "dec":
        string = xor_dec(sys.argv[2],sys.argv[1])
        print("Decoded string: "+string)
    
main()