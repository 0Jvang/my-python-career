def gettext():
    txt=open("hamlet.txt", "r").read()
    txt=txt.lower()
    for i in '!"#$%&()*+,-./:;<=>?@[\\]^_‘{|}~':
        txt=txt.replace(i," ")
    return txt
ham=gettext()
ham=ham.split()
counts={}
for i in ham:
    counts[i]=counts.get(i,0)+1
words=list(counts.items())
words.sort(key=lambda x:x[1],reverse=True)
for i in range(10):
    word,count=words[i]
    print("{:<10}{:>5}".format(word,count))
