import glob
print glob.glob("*.html")
arr = glob.glob("*.html")
i=0
k=[]
ray =[]
while i < len(arr):
    file = open(arr[i], "r")
    #print file.read()
    k.append(file.read())
    i = i+1
print k
'''
Outputs:
print print glob.glob("*.html")
['source.html', 'so.html']   
print k
['google.com', 'socorop.com'] 
'''
