import glob
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

while ll<len(k[0]):
    if k[0][ll] == "=":
        str1 = k[0]
        print str1[ll+1:len(k[0])]
    ll = ll + 1
'''
Outputs:
print print glob.glob("*.html")
['source.html', 'so.html']   
print k
['google.com', 'socorop.com'] 
'''
