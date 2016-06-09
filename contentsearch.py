import glob
from bs4 import BeautifulSoup
#print glob.glob("*.html")
arr = glob.glob("*.html")
i=0
ll=0
k=[]
ray =[]
str=""
while i < len(arr):
    file = open(arr[i], "r")
    #print file.read()
    k.append(file.read())
    i = i+1
print k
soup = BeautifulSoup(k[0],"html5lib")
for link in soup.findAll('a'):
    print link.get('href')
