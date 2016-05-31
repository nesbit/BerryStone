import binascii
import re
import os
schemes = [
	"http://www.",
	"https://wwww.",
	"http://",
	"https://"]
expansions = [
    ".com/", ".org/", ".edu/", ".net/", ".info/", ".biz/", ".gov/",
    ".com", ".org", ".edu", ".net", ".info", ".biz", ".gov"
        ]

def startBeacon(uri):
	i=0
	thisE=0
	k=0
	uriHex =""
	foundExpansion = False
	# this makes the URL Scheme
	for s in range(len(schemes)):
		thisScheme = schemes[s]
		if uri.startswith(thisScheme):
			print (thisScheme + "," + str(s))
			urlScheme = hex(s)[2:].zfill(2)
	print (uri)
	#this makes the Expansion
	while i < len(uri) and foundExpansion== False:
		if uri[i] == '.':
			for e in range(len(expansions)):
				thisExpansion = expansions[e]
				if uri.startswith(thisExpansion, i) and foundExpansion==False:
					print ("yes " + thisExpansion + " " + str(e))
					thisE = e
					foundExpansion = True
		i = i + 1
	#this puts the domain name in
	schemeLength = len(thisScheme)
	expansionLength = len(thisExpansion)
	uriString = uri[schemeLength:len(uri)-expansionLength]
	print (uriString)
	
	while k < len(uriString):
		uriHex=str(uriHex + " "+"{0:02x}".format(ord(uriString[k])))
		k=k+1
	#	print ("debug " +str(k) + uriHex)
	#chr() converts int to hex
	str1 = "02 01 1a 03 03 aa fe "+str(hex(len(uriString)+7)[2:].zfill(2))+" 16 aa fe "
	str2 = "10 ed " +urlScheme+""+ uriHex+" "+hex(thisE)[2:].zfill(2)
	str3 = str1 + str2
	print ("Length " + str(len(re.findall(r'\w+', str3))))
	
	str3 = hex(len(re.findall(r'\w+', str3)))[2:].zfill(2) +" "+ str3
	while len(re.findall(r'\w+', str3)) < 32: str3 = str3 + " 00"
	#str3 = str3.replace("\\x", " ")
	print ("Hello " + str3)
	#print (int(str3))
	os.system("sudo hcitool -i hci0 cmd 0x08 0x000a 00")
#Set message
	os.system("sudo hcitool -i hci0 cmd 0x08 0x0008 " + str3)
#Resume advertising
	os.system("sudo hcitool -i hci0 cmd 0x08 0x000a 01")
#def broadcast(message):

startBeacon("https://ert.com")
